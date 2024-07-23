from typing import List


def valid_mountain_array(arr: List[int]):
    if len(arr) < 3 or arr[0] >= arr[1]:
        print(False)
        return

    increasing = True
    for num in range(1, len(arr)):
        if arr[num] == arr[num - 1]:
            print(False)
            return
        elif not increasing and arr[num] > arr[num - 1]:
            print(False)
            return
        elif increasing and arr[num] < arr[num - 1]:
            increasing = False
    else:
        if increasing:
            print(False)
            return

    print(True)


valid_mountain_array([2, 1])
valid_mountain_array([3, 5, 5])
valid_mountain_array([0, 3, 2, 1])
valid_mountain_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
valid_mountain_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
