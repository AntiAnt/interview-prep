from solutions import IterativeSolution, ImprovedIterativeSolution
from typing import List

"""Solutions"""


def two_pointer_method(nums: List[int], val: int) -> int:
    i = 0
    n = len(nums)

    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]
            n -= 1
        else:
            i += 1
    return n


"""TESTS"""


def test_iterative_remove_elements_equal_to_value():
    s1 = IterativeSolution()

    tests = [
        {"nums": [3, 2, 2, 3], "val": 3, "expected": 2},
        {"nums": [0, 1, 2, 2, 3, 0, 4, 2], "val": 2, "expected": 5},
    ]

    for test in tests:
        kwargs = {k: v for k, v in test.items() if k != "expected"}
        num_not_value = s1.removeElement(**kwargs)
        expected = test["expected"]
        assert num_not_value == expected


def test_improved_iterative_remove_elements_equal_to_value():
    sol = ImprovedIterativeSolution()

    tests = [
        {"nums": [3, 2, 2, 3], "val": 3, "expected": 2},
        {"nums": [0, 1, 2, 2, 3, 0, 4, 2], "val": 2, "expected": 5},
    ]

    for test in tests:
        kwargs = {k: v for k, v in test.items() if k != "expected"}
        num_not_value = sol.removeElement(**kwargs)
        expected = test["expected"]
        print(tests)
        assert num_not_value == expected


def test_2_pointer_solution():
    tests = [
        {"nums": [3, 2, 2, 3], "val": 3, "expected": 2, "expected_array": [2, 2]},
        {
            "nums": [0, 1, 2, 2, 3, 0, 4, 2],
            "val": 2,
            "expected": 5,
            "expected_array": [0, 1, 3, 0, 4],
        },
    ]

    for test in tests:
        kwargs = {
            k: v for k, v in test.items() if k not in ["expected", "expected_array"]
        }
        num_not_value = two_pointer_method(**kwargs)
        nums_left = test["expected"]
        assert num_not_value == nums_left
