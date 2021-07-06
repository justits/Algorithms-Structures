import unittest
import math

from Slice import Slice
from ternary_search import ternary_search


def f_square(x):
    return x ** 2 + 6 * x + 2


def f_sin(x):
    return math.sin(x)


test_case_find = [
    (f_square, Slice(-6., 0.), -3),
    (f_sin, Slice(2., 6.), 3 * math.pi / 2),
    (f_sin, Slice(- 3 * math.pi / 2, 0.), -math.pi / 2)
]


class TestBisectionMethod(unittest.TestCase):
    def test_search(self):
        for fun, segment, ans in test_case_find:
            self.assertEqual(round(ternary_search(fun, segment), 5), round(ans, 5))
