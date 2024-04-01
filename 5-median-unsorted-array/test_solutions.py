import random
import pdb
from typing import List
from quickselect import get_median_from_quickselect_rewrite


def partition(nums: List[int], left: int, right: int, pivot_index: int) -> int:
    # partitions array in place, moving elements
    pivot_value = nums[pivot_index]
    # swap pivot_index with right index
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    store_index = left
    for i in range(left, right):
        if nums[i] < pivot_value:
            # swap current element with element at store_index
            nums[store_index], nums[i] = nums[i], nums[store_index]
            # increment store_index
            store_index += 1
    # swap the pivot to where it is left < pivot <= right
    nums[store_index], nums[right] = nums[right], nums[store_index]
    return store_index


def select(nums: List[int], left: int, right: int, k: int) -> int:
    if left == right:
        return nums[left]
    # random index from left to right
    pivot_index = random.randint(left, right)
    # partitions array and returns the new index of the random element selected.
    pivot_index = partition(nums=nums, left=left, right=right, pivot_index=pivot_index)

    if pivot_index == k:
        # need to account for even vs odd length arrays
        return nums[pivot_index]
    elif k < pivot_index:
        return select(nums=nums, left=left, right=pivot_index - 1, k=k)
    else:
        return select(nums=nums, left=pivot_index + 1, right=right, k=k)


def get_median(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    median_idx = (len(nums) - 1) // 2

    if len(nums) % 2 == 0:
        return (
            select(nums=nums, left=left, right=right, k=median_idx)
            + select(nums=nums, left=left, right=right, k=median_idx + 1)
        ) / 2
    else:
        return select(nums=nums, left=left, right=right, k=median_idx)


def test_get_median_of_unsorted_array() -> None:
    odd_test_array = [47, 65, 45, 24, 44, 7, 2, 100, 18, 70, 24, 60, 9]
    odd_median = 44
    even_test_array = [56, 17, 39, 39, 0, 83, 54, 78, 24, 90, 78, 45]
    even_median = 49.5

    assert get_median(odd_test_array) == odd_median
    assert get_median(even_test_array) == even_median


def test_get_median_rewrite_of_unsorted_array() -> None:
    odd_test_array = [47, 65, 45, 24, 44, 7, 2, 100, 18, 70, 24, 60, 9]
    odd_median = 44
    even_test_array = [56, 17, 39, 39, 0, 83, 54, 78, 24, 90, 78, 45]
    even_median = 49.5

    assert get_median_from_quickselect_rewrite(odd_test_array) == odd_median
    assert get_median_from_quickselect_rewrite(even_test_array) == even_median
