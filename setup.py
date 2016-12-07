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
from setuptools import setup
import sitemap_gen

setup(
    name="sitemap-gen",
    version="0.1.0",
    author="Junpei Kawamoto",
    author_email="kawamoto.junpei@gmail.com",
    description=sitemap_gen.__doc__,
    # py_modules=[""],
    test_suite="tests.suite",
    license="MIT",
    # keywords="cli helper",
    url="https://github.com/jkawamoto/sitemap-gen",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Utilities"
    ]
)
