from typing import List


def move_zeroes_v2(nums: List[int]):
    i = 0
    w = 0
    zeroes_count = 0
    while i < len(nums):
        if nums[i] != 0:
            nums[w] = nums[i]
            w += 1
        else:
            zeroes_count -= 1
        i += 1
    while zeroes_count < 0:
        nums[zeroes_count] = 0
        zeroes_count += 1
    print(nums)


def move_zeroes(nums: List[int]):
    w = 0
    i = 0
    while i < len(nums):
        if nums[i] != 0:
            nums[w], nums[i] = nums[i], nums[w]
            w += 1
        i += 1
    print(nums)


move_zeroes([0, 1, 0, 3, 12])
move_zeroes([0])
