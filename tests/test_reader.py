import unittest
import sys
import argparse
from uniconfig import Config, ConfigError


class TestReader(unittest.TestCase):
    def test_invalid_type(self):
        with self.assertRaises(ConfigError):
            c = Config(1)

    def test_keywords(self):
        c = Config(foo="FOO", bar=10)
        self.assertEqual(c.foo, "FOO")
        self.assertEqual(c.bar, 10)

    def test_dict(self):
        c = Config({"foo": "FOO", "bar": 10})
        self.assertEqual(c.foo, "FOO")
        self.assertEqual(c.bar, 10)

    def test_dict_num(self):
        c = Config({"1st": 1, 100: 100})
        self.assertEqual(c["1st"], 1)
        self.assertEqual(c[100], 100)

    def test_yaml(self):
        c = Config("""\
        foo: FOO
        bar: 10
        """)
        self.assertEqual(c.foo, "FOO")
        self.assertEqual(c.bar, 10)

    def test_json(self):
        c = Config("""{"foo": "FOO", "bar": 10 }""")
        self.assertEqual(c.foo, "FOO")
        self.assertEqual(c.bar, 10)

    def test_yaml_file(self):
        c = Config(open("./tests/files/config.yaml", "r"))
        self.assertEqual(c.foo, "FOO")
        self.assertEqual(c.bar, 10)

    def test_json_file(self):
        c = Config(open("./tests/files/config.json", "r"))
        self.assertEqual(c.foo, "FOO")
        self.assertEqual(c.bar, 10)

    def test_argparse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("foo", type=str)
        parser.add_argument("bar", type=int)
        parser.add_argument("--verbose", action="store_true")

        args = parser.parse_args(["FOO", "10", "--verbose"])
        c = Config(args)
        self.assertEqual(c.foo, "FOO")
        self.assertEqual(c.bar, 10)
        self.assertEqual(c.verbose, True)

    def test_argparse_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("foo", type=str)
        parser.add_argument("bar", type=int)
        parser.add_argument("--verbose", action="store_true")

        for arg in ["FOO", "10", "--verbose"]:
            sys.argv.append(arg)

        c = Config(parser)
        self.assertEqual(c.foo, "FOO")
        self.assertEqual(c.bar, 10)
        self.assertEqual(c.verbose, True)

    def test_mixture(self):
        d = {"foo": "f", "bar": 200, "baz": "baz"}
        j = """{"bar": 500}"""

        c = Config(d, j, foo="FOO")
        self.assertEqual(c.foo, "FOO")
        self.assertEqual(c.bar, 500)
        self.assertEqual(c.baz, "baz")

        c = Config(j, d)
        self.assertEqual(c.foo, "f")
        self.assertEqual(c.bar, 200)
        self.assertEqual(c.baz, "baz")
