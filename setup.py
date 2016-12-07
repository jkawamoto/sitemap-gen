#
# setup.py
#
# Copyright (c) 2016 Junpei Kawamoto
#
# This software is released under the MIT License.
#
# http://opensource.org/licenses/mit-license.php
#
"""Package information.
"""
from setuptools import setup, find_packages
import sitemap_gen


def load_requires_from_file(filepath):
    """Read a package list from a given file path.

    Args:
      filepath: file path of the package list.

    Returns:
      a list of package names.
    """
    with open(filepath) as fp:
        return [pkg_name.strip() for pkg_name in fp.readlines()]


setup(
    name="sitemap-gen",
    version="0.1.0",
    author="Junpei Kawamoto",
    author_email="kawamoto.junpei@gmail.com",
    description=sitemap_gen.__doc__,
    packages=find_packages(exclude=["tests"]),
    package_data={
        "sitemap_gen": ["sitemap.xml"]
    },
    scripts=["sitemap-gen"],
    install_requires=load_requires_from_file("requirements.txt"),
    test_suite="tests.suite",
    license="MIT",
    keywords="cli helper",
    url="https://github.com/jkawamoto/sitemap-gen",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Topic :: Utilities"
    ]
)
