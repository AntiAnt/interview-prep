from typing import List


def partition(_list: List[int], left: int, right: int, pivot_index: int, k: int) -> int:
    # partitions array in place, moving elements
    pivot_value = _list[pivot_index]
    # swap pivot_index with right index
    _list[pivot_index], _list[right] = _list[right], _list[pivot_index]
    store_index = left
    for i in range(left, right):
        if _list[i] < pivot_value:
            # swap current element with element at store_index
            _list[store_index], _list[i] = _list[i], _list[store_index]
            # increment store_index
            store_index += 1
    # swap the pivot to where it is left < pivot <= right
    _list[store_index], _list[right] = _list[right], _list[store_index]
    return store_index


def select(_list: List[int], left: int, right: int, k: int) -> int:
    while True:
        if left == right:
            return left

        pivot_idx = pivot(_list, left, right)
        pivot_idx = partition(_list, left, right, pivot_idx, k)

        if k == pivot_idx:
            return pivot_idx
        elif k < pivot_idx:
            right = pivot_idx - 1
        else:
            left = pivot_idx + 1


def partition_5(_list: List[int], left: int, right: int) -> int:
    i = left + 2

    while i <= right:
        j = i
        while j > left and _list[j - 1] > _list[j]:
            _list[j - 1], _list[j] = _list[j], _list[j - 1]
            j -= 1
        i += 1

    return left + (right - left) // 2


def pivot(_list: List[int], left: int, right: int) -> int:
    if right - left < 5:
        return partition_5(_list=_list, left=left, right=right)

    for i in range(left, right, 5):
        sub_right = i + 4 if i + 4 < right else right
        median_five = partition_5(_list, i, sub_right)
        _list[median_five], _list[left + ((i - left) // 5)] = (
            _list[left + ((i - left) // 5)],
            _list[median_five],
        )

    mid = ((right - left) // 10) + left + 1

    return select(_list=_list, left=left, right=((right - left) // 5), k=mid)


def get_median_of_medians(_list: List[int]) -> int:
    left, right = 0, len(_list) - 1
    median_idx = (len(_list) - 1) // 2

    if len(_list) % 2 == 0:
        left_median = _list[select(_list=_list, left=left, right=right, k=median_idx)]
        right_median = _list[select(_list=_list, left=left, right=right, k=median_idx + 1)]
        print(f"left: {left_median}, right: {right_median}, median: {(left_median + right_median) / 2}")
        return (left_median + right_median) / 2
    else:
        median = _list[select(_list=_list, left=left, right=right, k=median_idx)]
        print(f"median: {median}")
        return median
