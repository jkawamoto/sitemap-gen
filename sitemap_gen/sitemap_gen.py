#
# sitemap_gen.py
#
# Copyright (c) 2016 Junpei Kawamoto
#
# This software is released under the MIT License.
#
# http://opensource.org/licenses/mit-license.php
#
"""Generate a sitemap of a website managed in a git repository.
"""
import jinja2
import os
from os import path
import subprocess
import time
try:
    import urlparse
except ImportError:
    from urllib import parse as urlparse


TIME_FORMAT = "%Y-%m-%dT%H:%M:%S+00:00"
"""Time format.
"""


def find(root, tracked_files=False):
    """Looking for html files from a given root directory.

    Args:
      root: Path for the root directory where the traverse starts.
      tracked_files: If True, yields only tracked files.

    Yields:
      Relative path of found files from the given root dir.
    """
    if tracked_files:
        base = subprocess.check_output(["pwd"]).strip()
        for name in subprocess.check_output(["git", "ls-files"]).split("\n"):
            if name.endswith(".html"):
                p = path.join(base, name)
                if root == "." or p.startswith(root):
                    yield path.relpath(p, root)

    else:
        for dirpath, _, filenames in os.walk(root):
            for name in filenames:
                if name.endswith(".html"):
                    yield path.relpath(path.join(dirpath, name), root)


def mod_time(filepath):
    """Get the last modification of a given file path.

    The returned time means seconds from the epoch time.

    This method first checkes the given file are managed in the current git
    repository, and returns its last commit time if it is found in the repository.
    If the file isn't found in the repository, this method returns the last
    modification time using `os.path.getmtime`.

    Args:
      filepath: absolute path to be checked the last mod time.

    Returns:
      Integer value which means seconds from the epoch time.
    """
    try:
        return int(subprocess.check_output([
            "git", "--no-pager", "log", "--pretty=%at", "-n1", filepath]))
    except subprocess.CalledProcessError:
        return int(path.getmtime(filepath))
    except ValueError:
        return int(path.getmtime(filepath))


def generate(base_url, root, tracked_files=False):
    """Generate a site map of a web site of which root is given.

    Args:
      base_url: Base URL of the web site of which site map this function generates.
      root: Document root of the web site.
      tracked_files: If True, only tracked files will be included.

    Returns:
      String representing a site map.
    """
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(path.dirname(__file__), encoding='utf8'))
    tmpl = env.get_template("sitemap.xml")

    return tmpl.render(pages=[  # pylint: disable=E1101
        dict(
            url=urlparse.urljoin(base_url, filename),
            lastmod=time.strftime(
                TIME_FORMAT, time.gmtime(mod_time(path.join(root, filename))))
        )
        for filename in find(root, tracked_files)
    ])
