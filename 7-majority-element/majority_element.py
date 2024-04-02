from typing import List


def get_majority_element(nums: List[int]) -> int:
    counter = 0
    candidate = None
    for num in nums:
        if counter == 0:
            candidate = num
        
        counter += 1 if num == candidate else -1

    return candidate