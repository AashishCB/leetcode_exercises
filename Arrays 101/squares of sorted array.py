from typing import List


def get_sorted_squares_v1(nums: List[int]):
    sorted_squares = []
    index = 0
    num = 0
    while num < len(nums):
        if nums[num] < 0:
            sorted_squares.insert(index, nums[num] ** 2)
            num += 1
        else:
            squared_num = nums[num] ** 2
            if index == num or squared_num < sorted_squares[index]:
                sorted_squares.insert(index, squared_num)
                num += 1
            else:
                index += 1

    print(sorted_squares)


def get_sorted_squares(nums: List[int]):
    sorted_squares = len(nums) * [0]
    left = 0
    right = len(nums) - 1
    current = len(nums) - 1
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            sorted_squares[current] = nums[left] ** 2
            left += 1
        else:
            sorted_squares[current] = nums[right] ** 2
            right -= 1
        current -= 1
    print(sorted_squares)


# get_sorted_squares([-4, -1, 0, 3, 10])
get_sorted_squares([-7, -3, 2, 3, 11])
# get_sorted_squares([0, 3, 10])
# get_sorted_squares([2, 1])
