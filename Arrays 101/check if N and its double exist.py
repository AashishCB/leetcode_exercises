from typing import List


def check_if_exist_v2(arr: List[int]):
    exists = False
    for i in range(0, len(arr)):
        if arr.count(0) >= 2:
            exists = True
            break
        if arr[i] != 0 and ((arr[i] % 2 == 0 and arr[i] / 2 in arr) or arr[i] * 2 in arr):
            exists = True
            break
    print(exists)


def check_if_exist(arr: List[int]):
    exist = False
    seen = set()
    for num in arr:
        if num * 2 in seen or (num % 2 == 0 and num / 2 in seen):
            exist = True
            break
        seen.add(num)
    print(exist)


check_if_exist([10, 2, 5, 3])
check_if_exist([3, 1, 7, 11])
check_if_exist([-16, 13, 8])
check_if_exist([-2, 0, 10, -19, 4, 6, -8])
check_if_exist([0, 0])
