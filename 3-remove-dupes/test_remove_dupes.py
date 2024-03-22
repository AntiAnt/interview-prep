from typing import List

"""Solutions"""


def remove_duplicates(nums: List[int]) -> int:
    pointer = 1
    while pointer < len(nums):
        if nums[pointer] == nums[pointer - 1]:
            nums.pop(pointer)
        else:
            pointer += 1
    return len(nums)


"""Tests"""


def test_pointer_iteration() -> None:
    tests = [
        {"nums": [1, 1, 2], "expected": 2},
        {"nums": [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], "expected": 5},
    ]

    for test in tests:
        new_len = remove_duplicates(test.get("nums"))

        assert new_len == test["expected"]
