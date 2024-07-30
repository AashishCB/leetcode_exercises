from typing import List


def find_max_consecutive_ones(nums: List[int]):
    longest_sequence = 0
    left = 0
    right = 0
    num_zeroes = 0
    while right < len(nums):
        if nums[right] == 0:
            num_zeroes += 1
        while num_zeroes == 2:
            if nums[left] == 0:
                num_zeroes -= 1
            left += 1

        longest_sequence = max(longest_sequence, right - left + 1)
        right += 1

    print(nums)
    print(longest_sequence)


find_max_consecutive_ones([1, 0, 1, 1, 0])
find_max_consecutive_ones([1, 0, 1, 1, 0, 1])
find_max_consecutive_ones([1, 1, 0, 1])
find_max_consecutive_ones([1, 0, 0, 1, 1, 0, 1])
