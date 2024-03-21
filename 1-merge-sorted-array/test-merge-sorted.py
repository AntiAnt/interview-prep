from solution_1 import Solution1
from solution_2 import Solution2

test1 = [
    {
        "nums1": [1, 2, 3, 0, 0, 0],
        "m": 3,
        "nums2": [2, 5, 6],
        "n": 3,
        "expected": [1, 2, 2, 3, 5, 6],
    },
    {"nums1": [1], "m": 1, "nums2": [], "n": 0, "expected": [1]},
    {"nums1": [], "m": 0, "nums2": [2], "n": 1, "expected": [2]},
    {"nums1": [1, 2, 4, 0], "m": 3, "nums2": [2], "n": 1, "expected": [1, 2, 2, 4]},
]

s1 = Solution1()

for test in test1:
    kwargs = {k: i for k, i in test.items() if k != "expected"}
    s1.merge(**kwargs)
    expected = test["expected"]

    if test["nums1"] == expected:
        print("pass")
    else:
        print(f"fail-> answer: {test.nums1} != expected: {expected}")

test2 = [
    {
        "nums1": [1, 2, 3, 0, 0, 0],
        "m": 3,
        "nums2": [2, 5, 6],
        "n": 3,
        "expected": [1, 2, 2, 3, 5, 6],
    },
    {"nums1": [1], "m": 1, "nums2": [], "n": 0, "expected": [1]},
    {"nums1": [], "m": 0, "nums2": [2], "n": 1, "expected": [2]},
    {"nums1": [1, 2, 4, 0], "m": 3, "nums2": [2], "n": 1, "expected": [1, 2, 2, 4]},
]
s2 = Solution2()

for test in test2:
    kwargs = {k: i for k, i in test.items() if k != "expected"}
    s2.merge(**kwargs)
    expected = test["expected"]
    if test["nums1"] == expected:
        print("pass")
    else:
        print(f"fail-> answer: {test.nums1} != expected: {expected}")


print("SUCCESS !!!!!")
