import sys

test_case_sort = [
    [],
    [-1, -1, -1, -1],
    [0],
    ['t', 'a', 'v', 'r', 'z'],
    [1, 2, 3, 4, 5],
    [-1, -2, -3, -4, -5],
    [1.1, 1],
    [float('inf')],
    [float('-inf')],
    [sys.maxsize],
    [True, False, True],
    [None],
    [True, 10],
    ['test', 'c']
]

test_case_value = [
    [1, 'a', None, True],
    ['asd', True]
]
