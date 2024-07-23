from typing import List


def sort_array_by_parity(nums: List[int]):
    w = 0
    for r in range(0, len(nums)):
        if nums[r] % 2 == 0:
            nums[w], nums[r] = nums[r], nums[w]
            w += 1
    print(nums)


sort_array_by_parity([3, 1, 2, 4])
sort_array_by_parity([0])
