import unittest
import math

from bisection_method import bisection_method


def f_x(x):
    return x


def f_tg(x):
    return math.tan(x)


test_case_find = [
    (f_x, 0, 0),
    (f_x, 1, 1),
    (f_tg, 1, math.pi / 4),
    (f_tg, -1, -math.pi / 4)
]


class TestBisectionMethod(unittest.TestCase):
    def test_search(self):
        for fun, search_elem, ans in test_case_find:
            self.assertEqual(round(bisection_method(fun, search_elem), 8), round(ans, 8))
