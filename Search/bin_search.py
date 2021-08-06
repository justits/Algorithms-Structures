from Slice import Slice

EPS = 10e-10


def is_elem_in_list(sorted_list, searched_elem):
    def search_subarea(array_slice):
        if array_slice.len() == 1:
            return sorted_list[array_slice.left] == searched_elem

        med = int(array_slice.med())
        if searched_elem == sorted_list[med]:
            return True
        elif searched_elem < sorted_list[med]:
            return search_subarea(Slice(array_slice.left, med))
        else:
            return search_subarea(Slice(med + 1, array_slice.right))

    size_list = len(sorted_list)
    if size_list == 0 or searched_elem < sorted_list[0] or searched_elem > sorted_list[- 1]:
        return False
    return search_subarea(Slice(0, size_list))


def lower_bound(sorted_list, searched_elem):
    def search_subarea(array_slice):
        if array_slice.len() == 1:
            return array_slice.right

        med = int(array_slice.med())
        if searched_elem <= sorted_list[med]:
            return search_subarea(Slice(array_slice.left, med))
        else:
            return search_subarea(Slice(med, array_slice.right))

    size_list = len(sorted_list)
    if size_list == 0:
        return 0
    return search_subarea(Slice(-1, size_list))


def upper_bound(sorted_list, searched_elem):
    return lower_bound(sorted_list, searched_elem + EPS)
