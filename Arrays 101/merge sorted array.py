from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    p1 = m - 1
    p2 = n - 1
    k = m + n - 1
    while p2 >= 0:
        if p1 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[k] = nums1[p1]
                p1 -= 1
                k -= 1
            else:
                nums1[k] = nums2[p2]
                p2 -= 1
                k -= 1
        else:
            nums1[k] = nums2[p2]
            p2 -= 1
            k -= 1
        # print(nums1)
        # print(p2)
    print('final', nums1)


merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
merge(nums1=[1], m=1, nums2=[], n=0)
merge(nums1=[0], m=0, nums2=[1], n=1)
merge(nums1=[2, 0], m=1, nums2=[1], n=1)
