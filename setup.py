#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from io import open as io_open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__author__ = "Casper da Costa-Luis <casper.dcl@physics.org>"
__licence__ = "MPL-2.0"
__version__ = "0.0.0"
src_dir = os.path.abspath(os.path.dirname(__file__))

# Execute Makefile commands if specified
if sys.argv[1].lower().strip() == "make":
    import pymake

    fpath = os.path.join(src_dir, "Makefile")
    pymake.main(["-f", fpath] + sys.argv[2:])
    sys.exit(0)

README_rst = ""
fndoc = os.path.join(src_dir, "README.rst")
with io_open(fndoc, mode="r", encoding="utf-8") as fd:
    README_rst = fd.read()
setup(
    name="shtab",
    version=__version__,
    description="Automatically generate shell tab completion scripts"
    " for python CLI apps",
    long_description=README_rst,
    license=__licence__,
    author=__author__.split("<")[0].strip(),
    author_email=__author__.split("<")[1][:-1],
    url="https://github.com/iterative/shtab",
    platforms=["any"],
    packages=["shtab"],
    provides=["shtab"],
    install_requires=["argparse"],
    extras_require={"dev": ["pre-commit", "py-make>=0.1.0", "twine"]},
    entry_points={"console_scripts": ["shtab=shtab:main.main"]},
    package_data={"shtab": ["LICENCE"]},
    python_requires=">=2.7, !=3.0.*, !=3.1.*",
    classifiers=[
        # Trove classifiers
        # (https://pypi.org/pypi?%3Aaction=list_classifiers)
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: MacOS X",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Other Audience",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: BSD :: FreeBSD",
        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX :: SunOS/Solaris",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: IronPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Unix Shell",
        "Topic :: Desktop Environment",
        "Topic :: Education :: Computer Aided Instruction (CAI)",
        "Topic :: Education :: Testing",
        "Topic :: Office/Business",
        "Topic :: Other/Nonlisted Topic",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Pre-processors",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Shells",
        "Topic :: Terminals",
        "Topic :: Utilities",
    ],
    keywords="tab complete completion shell bash zsh argparse",
    tests_require=["flake8", "black"],
)