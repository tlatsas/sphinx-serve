# -*- coding: utf-8 -*-
"""
sphinx-serve
------------

Simple utility to easier preview your sphinx documentation.

After running the sphinx-serve command, it tries to detect the
sphinx build directory. It examines the current working directory
and if the build directory is not present, it tries to iterate
the parent paths. If a build directory is detected it launches
an http server.

The build directory name is configurable. It also supports serving
documentation from the html folder of the singlehtml folder.

Installation
------------

    pip install sphinx-serve

Usage
-----

Run with:

    sphinx-serve

For all available options use:

    sphinx-serve --help

"""
from setuptools import setup 
import sphinx_serve

setup(
    name="sphinx-serve",
    version=sphinx_serve.__version__,
    description=sphinx_serve.__doc__.strip(),
    long_description=__doc__,
    url="https://github.com/tlatsas/sphinx-serve",
    author="Tasos Latsas",
    author_email="tlatsas@gmx.com",
    license="MIT",
    packages=["sphinx_serve"],
    entry_points = {
        "console_scripts": [
            "sphinx-serve = sphinx_serve.__main__:main",
        ],
    },
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
        "Topic :: Documentation",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License"
    ],
)
