import sys
import unittest
import random

import bin_search

test_case_find = [
    ([], 10, (False, 0, 0)),
    ([-1, -1, -1, -1], -1, (True, 0, 4)),
    ([-1, -1, -1, -1], 1, (False, 4, 4)),
    ([-10, -1, 0, 3], -10, (True, 0, 1)),
    ([-5, -4, -3, -2, -1], 0, (False, 5, 5)),
    ([1, 2, 3, 4, 5], 1, (True, 0, 1)),
    ([False, True, True], True, (True, 1, 3)),
    ([sys.maxsize], sys.maxsize, (True, 0, 1)),
    ([True, 10], 1, (True, 0, 1)),
    ([1, 1.1, 1.1, 1.2, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.4, 1.5, 2.1], 1.3, (True, 4, 11))
]

test_case_value = [
    [1, 'a', None, True],
    ['asd', True]
]


class TestBinSearch(unittest.TestCase):
    def test_bin_search(self):
        for a, k, (is_in, lb, ub) in test_case_find:
            self.assertEqual(bin_search.is_elem_in_list(a, k), is_in)
            self.assertEqual(bin_search.lower_bound(a, k), lb)
            self.assertEqual(bin_search.upper_bound(a, k), ub)

    def test_values(self):
        for a in test_case_value:
            self.assertRaises(TypeError, bin_search.is_elem_in_list, (a, random.randint(0, len(a) - 1)))
