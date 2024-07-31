from typing import List


def find_dominant_index(nums: List[int]):
    dominant_value_index = 0
    dominant_value = 0
    second_dominant_value = 0
    for i, val in enumerate(nums):
        if val > dominant_value:
            second_dominant_value = dominant_value
            dominant_value = nums[i]
            dominant_value_index = i
        elif val > second_dominant_value:
            second_dominant_value = val
    if dominant_value >= second_dominant_value * 2:
        print(dominant_value_index)
    else:
        print(-1)


find_dominant_index([1, 2, 3, 4])
find_dominant_index([3, 6, 1, 0])
find_dominant_index([0, 0, 3, 2])
