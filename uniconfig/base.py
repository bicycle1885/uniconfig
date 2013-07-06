"""
Base uniconfig class
~~~~~~~~~~~~~~~~~~~~
"""


import argparse
import yaml
from .exceptions import ConfigError, CheckError
from .check import check_required

class Config(object):
    """The base class of configuration."""

    required = []

    def __init__(self, *args, **kwargs):
        self._attrs = {}

        for arg in args:
            self._process_arg(arg)

        if kwargs:
            self._process_arg(kwargs)

        self._check()

    def _process_arg(self, arg):
        if   isinstance(arg, dict):
            self._dict(arg)
        elif isinstance(arg, str):
            self._str(arg)
        elif isinstance(arg, file):
            self._file(arg)
        elif isinstance(arg, argparse.ArgumentParser):
            self._dict(vars(arg.parse_args()))
        elif isinstance(arg, argparse.Namespace):
            self._dict(vars(arg))
        else:
            raise ConfigError, "{} is not supported".format(type(arg))

    def _dict(self, d):
        for key in d:
            self._attrs[key] = d[key]

    def _str(self, s):
        self._dict(yaml.load(s))

    def _file(self, f):
        self._str(f.read())

    def _check(self):
        if self.required and not check_required(self.required, self._attrs.keys()):
            raise CheckError, "requirement is not satisfied"

    def __getattr__(self, key):
        val = self._attrs.get(key)
        if val is not None:
            return val
        else:
            raise AttributeError, ("'{klass}' object has no attribute '{attr}'"
                                   .format(klass=self.__class__.__name__,
                                           attr=key))

    def __getitem__(self, key):
        return self._attrs[key]

    def __len__(self):
        return len(self._attrs)

    def __iter__(self):
        return iter(self._attrs)

    def get(self, key):
        return self._attrs.get(key)
