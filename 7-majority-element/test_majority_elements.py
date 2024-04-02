from majority_element import get_majority_element

tests = [
    {"nums": [3, 2, 3], "expected": 3},
    {"nums": [2, 2, 1, 1, 1, 2, 2], "expected": 2},
]


def test_majority_elements() -> None:
    for test in tests:
        assert get_majority_element(test["nums"]) == test["expected"]
