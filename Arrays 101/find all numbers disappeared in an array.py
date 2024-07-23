from typing import List


def find_disappeared_numbers_v2(nums: List[int]):
    disappeared_numbers = set(range(1, len(nums)+1))
    for num in nums:
        disappeared_numbers.discard(num)
    print(disappeared_numbers)


def find_disappeared_numbers(nums: List[int]):
    n = len(nums)
    for i in range(0, n):
        index = abs(nums[i]) - 1
        nums[index] = abs(nums[index]) * -1
    print(nums)

    res = []
    for i in range(0, n):
        if nums[i] > 0:
            res.append(i+1)
    print(res)


find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1])
find_disappeared_numbers([1, 1])
