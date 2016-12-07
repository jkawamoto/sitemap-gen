"""Unit test for sitemap_gen module.
"""
from __future__ import absolute_import
import os
from os import path
import tempfile
import unittest

import sitemap_gen

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


if __name__ == "__main__":
    unittest.main()
