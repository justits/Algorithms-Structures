from Slice import Slice

EPS = 10e-10


def bisection_method(mono_increasing_fun, search_elem):
    array_slice = Slice(-1., 1.)
    while mono_increasing_fun(array_slice.left) > search_elem:
        array_slice.left *= 2
    while mono_increasing_fun(array_slice.right) < search_elem:
        array_slice.right *= 2

    min_decreasing_slice = array_slice.len() / EPS
    num_of_iter = 0
    decreasing_slice = 1
    while decreasing_slice < min_decreasing_slice:
        num_of_iter += 1
        decreasing_slice *= 2

    for i in range(num_of_iter):
        med = array_slice.med()
        if mono_increasing_fun(med) < search_elem:
            array_slice.left = med
        else:
            array_slice.right = med

    return array_slice.right
