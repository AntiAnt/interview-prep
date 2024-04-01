import random
from typing import List


def partition(arr: List[int], left: int, right: int, pivot_idx: int) -> int:
    pivot_value = arr[pivot_idx]
    arr[pivot_idx], arr[right] = (
        arr[right],
        arr[pivot_idx],
    )  # swap pivot to end of array
    pointer = left

    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[pointer], arr[i] = arr[i], arr[pointer]
            pointer += 1

    arr[pointer], arr[right] = arr[right], arr[pointer]
    return pointer


def select(arr: List[int], left: int, right: int, k: int) -> int:
    if left == right:
        return arr[left]

    pivot_idx = random.randint(left, right)
    pivot_idx = partition(arr, left, right, pivot_idx)

    if k == pivot_idx:
        return arr[pivot_idx]
    elif k < pivot_idx:
        return select(arr, left, pivot_idx - 1, k)
    else:
        return select(arr, pivot_idx + 1, right, k)


def get_median_from_quickselect_rewrite(arr: List[int]) -> int:
    """Rewite of median search from scratch"""
    left, right = 0, len(arr) - 1
    k = (len(arr) - 1) // 2

    if len(arr) % 2 == 0:
        return (
            select(arr=arr, left=left, right=right, k=k)
            + select(arr=arr, left=left, right=right, k=k + 1)
        ) / 2
    else:
        return select(arr=arr, left=left, right=right, k=k)
