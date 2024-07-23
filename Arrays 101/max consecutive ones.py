from typing import List


def find_max_consecutive_ones(nums: List[int]):
    max_count = 0
    count = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    print(max_count)


find_max_consecutive_ones([1, 1, 0, 1, 1, 1])
find_max_consecutive_ones([1, 0, 1, 1, 0, 1])
