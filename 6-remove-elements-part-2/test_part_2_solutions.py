from v2_solutions import remove_dupes_v2


tests = [
    {"nums": [1, 1, 1, 2, 2, 3], "expected_len": 5, "expected_order": [1, 1, 2, 2, 3]},
    {
        "nums": [0, 0, 1, 1, 1, 1, 2, 3, 3],
        "expected_len": 7,
        "expected_order": [0, 0, 1, 1, 2, 3, 3],
    },
]


def test_remove_elements_v2() -> None:
    for test in tests:
        len_processed = remove_dupes_v2(test["nums"])

        assert len_processed == test["expected_len"]
        for i in range(len(test["expected_order"])):
            assert test["nums"][i] == test["expected_order"][i]
