#! /usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name="python-irclib3",
      version="0.4.8",
      py_modules=["irclib", "ircbot"],
      author="Joel Rosdahl",
      author_email="joel@rosdahl.net",
      url="http://python-irclib.sourceforge.net")
