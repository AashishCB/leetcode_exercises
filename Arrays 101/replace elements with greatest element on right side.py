from typing import List


def replace_elements(arr: List[int]):

    i = len(arr) - 1
    highest_on_right = arr[-1]
    while i >= 0:
        temp = arr[i-1]
        arr[i-1] = highest_on_right
        if temp > highest_on_right:
            highest_on_right = temp
        i -= 1
    arr[i] = -1
    print(arr)


replace_elements([17, 18, 5, 4, 6, 1])
replace_elements([400])
