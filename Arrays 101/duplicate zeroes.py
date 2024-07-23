from typing import List


def duplicate_zeroes_v1(arr: List[int]) -> None:
    num = 0
    while num <= len(arr) - 1:
        if arr[num] != 0:
            num += 1
        else:
            for i in range(len(arr) - 1, num, -1):
                arr[i] = arr[i - 1]
            arr[num] = 0
            num += 2

    print(arr)


def duplicate_zeroes(arr: List[int]) -> None:
    zeroes_count = 0
    length = len(arr)
    num = 0
    while num < length - zeroes_count:
        if arr[num] == 0:
            zeroes_count += 1
        num += 1

    if arr[num - 1] == 0 and num-1 == length - zeroes_count:
        arr[length - 1] = 0
        length -= 1
        zeroes_count -= 1

    for i in range(length - zeroes_count - 1, -1, -1):
        if arr[i] == 0:
            arr[i + zeroes_count] = 0
            zeroes_count -= 1
            arr[i + zeroes_count] = 0
        else:
            arr[i + zeroes_count] = arr[i]
    print('final', arr)


duplicate_zeroes([1, 0, 2, 3, 0, 4, 5, 0])
duplicate_zeroes([1, 2, 3])
duplicate_zeroes([1, 5, 2, 0, 6, 8, 0, 6, 0])
duplicate_zeroes([8, 4, 5, 0, 0, 0, 0, 7])
