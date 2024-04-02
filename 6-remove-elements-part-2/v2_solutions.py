from typing import List


def remove_dupes_v2(nums: List[int]) -> int:
    pointer = 1
    right = len(nums) - 1

    while pointer < right:
        if (
            nums[pointer + 1] == nums[pointer]
            and nums[pointer + 1] == nums[pointer - 1]
        ):
            dupe = nums.pop(pointer)
            nums.append(dupe)
            right -= 1
        else:
            pointer += 1

    return pointer + 1  # +1 to get length of processed array
