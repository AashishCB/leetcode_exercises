from typing import List


def count_length(num: int) -> int:
    length = 0
    while num > 0:
        num = num // 10
        length = length + 1
    return length


def find_numbers(nums: List[int]) -> int:
    even_count = 0
    for num in nums:
        if count_length(num) % 2 == 0:
            even_count += 1
    return even_count
