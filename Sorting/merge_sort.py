def merge(left, right):
    merged = []
    i = 0
    j = 0
    left_size = len(left)
    right_size = len(right)
    while i + j < left_size + right_size:
        if j == right_size or (i < left_size and left[i] < right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged


def merge_sort(a):
    size_a = len(a)
    if size_a <= 1:
        return a
    left = merge_sort(a[:size_a // 2])
    right = merge_sort(a[size_a // 2:])
    return merge(left, right)
