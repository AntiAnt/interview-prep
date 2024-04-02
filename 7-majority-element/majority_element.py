from typing import List


def get_majority_element(nums: List[int]) -> int:
    counter = 0
    candidate = None
    for num in nums:
        if counter == 0:
            candidate = num
        
        if num == candidate:
            counter += 1
        else:
            coutner -= 1

    return candidate