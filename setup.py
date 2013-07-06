#!/usr/bin/env python

from setuptools import setup, find_packages
import uniconfig


setup(
    name="uniconfig",
    version=uniconfig.__version__,
    author=uniconfig.__author__,
    maintainer=uniconfig.__maintainer__,
    description="Make it easy to make configuration objects from any sources.",
    packages=find_packages(),
    install_requires=["PyYAML>=3.0"]
)
