from typing import List


def find_pivot_index_v1(nums: List[int]):
    n = len(nums)
    left_sum = [0] * n
    right_sum = [0] * n
    for i in range(1, n):
        left_sum[i] = left_sum[i-1] + nums[i-1]
        right_sum[-1-i] = right_sum[-i] + nums[-i]

    for i in range(0, n):
        if left_sum[i] == right_sum[i]:
            print(i)
            break
    else:
        print(-1)
    print(left_sum)
    print(right_sum)


def find_pivot_index(nums: List[int]):
    left_sum, right_sum = 0, sum(nums)
    for i, val in enumerate(nums):
        right_sum -= val
        if left_sum == right_sum:
            print(i)
            break
        left_sum += val
    else:
        print(-1)


find_pivot_index([1, 7, 3, 6, 5, 6])
find_pivot_index([1, 2, 3])
find_pivot_index([2, 1, -1])
