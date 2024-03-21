class Solution1(object):
    def merge(self, nums1, m, nums2, n):
        if m == 0:
            del nums1[:]
            nums1.extend(nums2)
            return

        if m < len(nums1):
            del nums1[m:]

        if n == 0:
            return

        nums1.extend(nums2)
        nums1.sort()
        return  