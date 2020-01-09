import math
import unittest
from parameterized import parameterized
from .fermat import factorize


class TestFermat(unittest.TestCase):

    @parameterized.expand([
        [5959],
        [123],
        [132773],
        [963129],
    ])
    def test_fermat(self, value):
        c, d = factorize(value)
        a, b = (c + d) / 2, (c - d) / 2
        self.assertEqual(value, a**2 - b**2)
        self.assertTrue(a.is_integer())
        self.assertTrue(b.is_integer())


if __name__ == '__main__':
    unittest.main()
