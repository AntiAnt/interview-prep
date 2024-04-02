import random
import pdb
from typing import List
from median_of_medians import get_median_of_medians


def test_get_median_rewrite_of_unsorted_array() -> None:
    odd_test_array = [47, 65, 45, 24, 44, 7, 2, 100, 18, 70, 24, 60, 9]
    odd_median = 44
    even_test_array = [56, 17, 39, 39, 0, 83, 54, 78, 24, 90, 78, 45]
    even_median = 49.5

    assert get_median_of_medians(odd_test_array) == odd_median
    assert get_median_of_medians(even_test_array) == even_median
