# sitemap-gen
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)
[![Build Status](https://travis-ci.org/jkawamoto/sitemap-gen.svg?branch=master)](https://travis-ci.org/jkawamoto/sitemap-gen)
[![PyPi](https://img.shields.io/badge/sitemap-gen-0.1.0-lightgrey.svg)](https://pypi.python.org/pypi?:action=display&name=sitemap-gen)

Generate a sitemap of a website managed in a git repository.

This tool generates `sitemap.xml` from a given document root
(by default the document root is the current directory).
To determine last modification time of each html file,
this tool uses the git commit log of those files.  


## Install

```
$ pip install --upgrade sitemap-gen
```


## Usage

~~~
sitemap-gen [-h] [--root ROOT] [--output OUTPUT] base

Generate a sitemap of a website managed in a git repository.

positional arguments:
  base             Base URL of the web site.

optional arguments:
  -h, --help       show this help message and exit
  --root ROOT      Document root of the web site. (Default: current dir)
  --output OUTPUT  Output filename. (Default: sitemap.xml)
~~~


## License
This software is released under the MIT License, see [LICENSE](LICENSE).
