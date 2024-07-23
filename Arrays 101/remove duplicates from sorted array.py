from typing import List


def remove_duplicates(nums: List[int]):
    k = 0
    p1 = 1
    while p1 < len(nums):
        if nums[k] != nums[p1]:
            k += 1
            nums[k] = nums[p1]
        p1 += 1
    print(k+1, nums)


remove_duplicates([1, 1, 2])
remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
