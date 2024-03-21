class Solution2(object):
    def merge(self, nums1, m, nums2, n):
        if m == 0:
            del nums1[:]
            nums1.extend(nums2)
            return

        if m < len(nums1):
            del nums1[m:]

        if n == 0:
            return

        p1 = 0
        p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                nums1.insert(p1, nums2[p2])
                p1 += 1
                p2 += 1

        while p2 < len(nums2):
            nums1.append(nums2[p2])
            p2 += 1

        return
