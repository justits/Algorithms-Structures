import random


def quick_sort(a):
    def split(left, right, pivot):
        pivot_left = left
        for i in range(left, right):
            if a[i] < pivot:
                a[pivot_left], a[i] = a[i], a[pivot_left]
                pivot_left += 1

        pivot_right = pivot_left
        for i in range(pivot_left, right):
            if a[i] == pivot:
                a[pivot_right], a[i] = a[i], a[pivot_right]
                pivot_right += 1
        return pivot_left, pivot_right

    def quick_sort_subarea(left, right):
        if right - left > 1:
            pivot = a[random.randint(left, right - 1)]
            pivot_left, pivot_right = split(left, right, pivot)
            quick_sort_subarea(left, pivot_left)
            quick_sort_subarea(pivot_right, right)

    quick_sort_subarea(0, len(a))
    return a
