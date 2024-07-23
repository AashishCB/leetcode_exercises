from typing import List


def height_checker_v2(heights: List[int]):
    expected = sorted(heights)
    count = 0
    for r in range(0, len(heights)):
        if heights[r] != expected[r]:
            count += 1

    print(count)


def height_checker(heights: List[int]):
    expected = [0] * len(heights)
    count = [0] * 101
    for i in heights:
        count[i] += 1

    h = 0
    for i in range(1, 101):
        for j in range(0, count[i]):
            expected[h] = i
            h += 1
    print(expected)

    res = 0
    for r in range(0, len(heights)):
        if heights[r] != expected[r]:
            res += 1

    print(res)


height_checker([1, 1, 4, 2, 1, 3])
height_checker([5, 1, 2, 3, 4])
height_checker([1, 2, 3, 4, 5])
