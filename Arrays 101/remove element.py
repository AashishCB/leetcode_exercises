from typing import List


def remove_element(nums: List[int], val: int):
    p1 = 0
    k = 0
    while p1 < len(nums):
        if nums[p1] != val:
            nums[k] = nums[p1]
            k += 1
        p1 += 1
    print(k, nums)


remove_element([3, 2, 2, 3], 3)
remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2)
