from typing import List


def running_sum_v1(nums: List[int]):
    res = []
    total = 0
    for i in range(0, len(nums)):
        total += nums[i]
        res.append(total)
    print(res)


def running_sum_v2(nums: List[int]):
    total = 0
    for i in range(0, len(nums)):
        total += nums[i]
        nums[i] = total
    print(nums)


def running_sum(nums: List[int]):
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i-1]
    print(nums)


running_sum([1, 2, 3, 4])
running_sum([1, 1, 1, 1, 1])
running_sum([3, 1, 2, 10, 1])
