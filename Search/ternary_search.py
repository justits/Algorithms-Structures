EPS = 10e-10


def ternary_search(fun, segment):
    min_decreasing_range = segment.len() / EPS
    num_of_iter = 0
    decreasing_range = 1
    while decreasing_range < min_decreasing_range:
        num_of_iter += 1
        decreasing_range *= 2

    for _ in range(num_of_iter):
        med = segment.med()
        if fun(med - EPS) < fun(med + EPS):
            segment.right = med + EPS
        else:
            segment.left = med - EPS
    return segment.right
