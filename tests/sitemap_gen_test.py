#
# sitemap_gen_test.py
#
# Copyright (c) 2016 Junpei Kawamoto
#
# This software is released under the MIT License.
#
# http://opensource.org/licenses/mit-license.php
#
"""Unit test for sitemap_gen module.
"""
from __future__ import absolute_import, print_function
import os
from os import path
import subprocess
import tempfile
import time
import unittest
from xml.etree import ElementTree

from sitemap_gen import sitemap_gen

HTMLDIR = path.join(path.dirname(__file__), "html")


class TestFind(unittest.TestCase):
    """Test case for finding html files.
    """

    def setUp(self):
        """Set up the test case.
        """
        with tempfile.NamedTemporaryFile(
                suffix=".html", dir=HTMLDIR, delete=False) as fp:
            self.path = fp.name

    def tearDown(self):
        """Tear down the test case.
        """
        os.remove(self.path)

    def test(self):
        """Test find function returns `index.html`, `sub.html`, and a temp file.
        """
        res = set(sitemap_gen.find(HTMLDIR))
        self.assertIn("./index.html", res)
        self.assertIn("sub/sub.html", res)
        self.assertIn("./" + path.basename(self.path), res)


class TestModTime(unittest.TestCase):
    """Test case for obtaining modified times.
    """

    def setUp(self):
        """Set up the test case.
        """
        with tempfile.NamedTemporaryFile(
                suffix=".html", dir=HTMLDIR, delete=False) as fp:
            self.path = fp.name

    def tearDown(self):
        """Tear down the test case.
        """
        os.remove(self.path)

    def test_index(self):
        """Obtaining the modified time of `index.html`.
        """
        res = sitemap_gen.mod_time(path.join(HTMLDIR, "./index.html"))
        ans = int(subprocess.check_output([
            "git", "--no-pager", "log", "--pretty=%at", "-n1",
            path.join(HTMLDIR, "index.html")
        ]))
        self.assertEqual(res, ans)

    def test_new_file(self):
        """Obtaining the modified time of a temporal file.
        """
        res = sitemap_gen.mod_time(self.path)
        self.assertEqual(res, int(path.getmtime(self.path)))


class TestSitemapGen(unittest.TestCase):
    """Test case for generating a site map.
    """

    def setUp(self):
        """Set up the test case.
        """
        with tempfile.NamedTemporaryFile(
                suffix=".html", dir=HTMLDIR, delete=False) as fp:
            self.path = fp.name

    def tearDown(self):
        """Tear down the test case.
        """
        os.remove(self.path)

    def test(self):
        """Generating a site map.
        """
        base_url = "https://jkawamoto.github.io/sitemap-gen/"
        res = sitemap_gen.generate(base_url, HTMLDIR)
        print(res)

        root = ElementTree.fromstring(res)
        self.assertEqual(root.tag, self.tagname("urlset"))

        for elem in root:
            self.assertEqual(elem.tag, self.tagname("url"))
            loc = elem.findtext(self.tagname("loc"))[len(base_url):]
            mod = time.strftime(
                sitemap_gen.TIME_FORMAT,
                time.gmtime(sitemap_gen.mod_time(path.join(HTMLDIR, loc))))
            self.assertEqual(elem.findtext(self.tagname("lastmod")), mod)

    @staticmethod
    def tagname(tag):
        """Get a normalized tag name.
        """
        return "{http://www.sitemaps.org/schemas/sitemap/0.9}" + tag


if __name__ == "__main__":
    unittest.main()
