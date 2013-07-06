import unittest
from uniconfig import Config


class TestGetter(unittest.TestCase):
    def setUp(self):
        self.config = Config(foo="FOO", bar=10)

    def test_attr(self):
        self.assertEqual(self.config.foo, "FOO")

    def test_attr_none(self):
        with self.assertRaises(AttributeError):
            self.config.none

    def test_get(self):
        self.assertEqual(self.config.get("foo"), "FOO")

    def test_get_none(self):
        self.assertEqual(self.config.get("none"), None)

    def test_get_item(self):
        self.assertEqual(self.config["foo"], "FOO")

    def test_get_item_none(self):
        with self.assertRaises(KeyError):
            self.config["none"]

    def test_iter(self):
        self.assertItemsEqual(self.config, ["foo", "bar"])

    def test_len(self):
        self.assertEqual(len(self.config), 2)
