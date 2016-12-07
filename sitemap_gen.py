#! /usr/bin/env python
"""Generate a sitemap of a website managed in a git repository.
"""
import os
from os import path
import subprocess


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
