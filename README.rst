uniconfig - Make it easy to make configuration objects from any sources
=======================================================================

``uniconfig`` bundles configurations from heterogeneous sources and make a configuration object.

.. code-block:: pycon

    >>> from uniconfig import Config
    >>> dictionary = {"one": 1, "two": 200}
    >>> yaml = """
    ... two: 2
    ... three: 300
    ... """
    >>> config = Config(dictionary, yaml, three=3)
    >>> config.one
    1
    >>> config.two
    2
    >>> config.three
    3

Sources
-------

Key-value structured objects are available like:

- keyword arguments
- dict
- yaml string/file
- json string/file
- argparse.ArgumentParser/argparse.Namespace


You can access configuration values through:

- attributes
- ``config["key"]``
- ``config.get("key")``


.. code-block:: pycon

    >>> config.one
    1
    >>> config["two"]
    2
    >>> config.get("three")
    3
