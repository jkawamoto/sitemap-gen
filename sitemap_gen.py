#! /usr/bin/env python
"""Generate a sitemap of a website managed in a git repository.
"""
import os
from os import path

def find(root):
    """Looking for html files from a given root directory.

    Args:
      root: Path for the root directory where the traverse starts.

    Yields:
      Relative path of found files from the given root dir.
    """
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            if name.endswith(".html"):
                yield path.join(path.relpath(dirpath, root), name)
