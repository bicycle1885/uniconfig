import unittest
from uniconfig import Config, CheckError


class TestChecker(unittest.TestCase):
    def test_and(self):
        class AndConfig(Config):
            required = ("foo", "bar")

        try:
            c = AndConfig(foo="FOO", bar=10)
        except Exception as e:
            self.fail(e)

        with self.assertRaises(CheckError):
            AndConfig(foo="FOO")

        with self.assertRaises(CheckError):
            AndConfig(bar=10)

    def test_or(self):
        class OrConfig(Config):
            required = ["foo", "bar"]

        try:
            c = OrConfig(foo="FOO")
        except Exception as e:
            self.fail(e)

        try:
            c = OrConfig(bar=10)
        except Exception as e:
            self.fail(e)

        with self.assertRaises(CheckError):
            OrConfig(baz="BAZ")

    def test_depends(self):
        class DependConfig(Config):
            required = ["foo", {"bar": "baz"}]

        try:
            c = DependConfig(foo="FOO")
        except Exception as e:
            self.fail(e)

        try:
            c = DependConfig(bar="BAR", baz="BAZ")
        except Exception as e:
            self.fail(e)

        with self.assertRaises(CheckError):
            DependConfig(bar="BAR")

    def test_complex(self):
        class ComplexConfig(Config):
            required = ("mode",
                        ["http", "smtp"],
                        {"http": ["url", "uri"],
                         "smtp": ("smtp_user", "smtp_passwd")})

        try:
            c = ComplexConfig(mode=0, http=True, uri="http://example.com")
        except Exception as e:
            self.fail(e)

        try:
            c = ComplexConfig(mode=0, smtp=True, smtp_user="joe", smtp_passwd="joe")
        except Exception as e:
            self.fail(e)

        with self.assertRaises(CheckError):
            ComplexConfig(mode=1)

        with self.assertRaises(CheckError):
            ComplexConfig(http=True, url="http://example.com")

        with self.assertRaises(CheckError):
            ComplexConfig(mode=1, http=True)

        with self.assertRaises(CheckError):
            ComplexConfig(mode=1, smtp=True)

        with self.assertRaises(CheckError):
            ComplexConfig(mode=1, smtp=True, smtp_passwd="pass")
