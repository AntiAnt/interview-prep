from solutions import IterativeSolution


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
