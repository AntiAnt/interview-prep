class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        raise NotImplementedError


class IterativeSolution(Solution):
    def removeElement(self, nums, val):
        p = 0

        while p < len(nums):
            if nums[p] == val:
                nums.pop(p)
            else:
                p += 1
        return len(nums)


class ImprovedIterativeSolution(Solution):
    def removeElement(self, nums, val):
        filtered = [i for i in nums if i != val]
        del nums[:]
        nums += filtered

        return len(nums)
