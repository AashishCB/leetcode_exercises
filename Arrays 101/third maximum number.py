from typing import List


def third_max_v2(nums: List[int]):
    max_list = [nums[0]]
    length_of_max_list = 1
    for r in range(1, len(nums)):
        if nums[r] in max_list:
            continue
        if length_of_max_list == 1:
            if nums[r] > max_list[0]:
                max_list.append(max_list[0])
                length_of_max_list += 1
                max_list[0] = nums[r]
            elif nums[r] < max_list[0]:
                max_list.append(nums[r])
                length_of_max_list += 1
        elif length_of_max_list == 2:
            if nums[r] > max_list[0]:
                max_list.append(max_list[1])
                length_of_max_list += 1
                max_list[1] = max_list[0]
                max_list[0] = nums[r]
            elif nums[r] > max_list[1]:
                max_list.append(max_list[1])
                length_of_max_list += 1
                max_list[1] = nums[r]
            elif nums[r] < max_list[1]:
                max_list.append(nums[r])
                length_of_max_list += 1
        elif length_of_max_list == 3:
            if nums[r] > max_list[0]:
                max_list[2] = max_list[1]
                max_list[1] = max_list[0]
                max_list[0] = nums[r]
            elif nums[r] > max_list[1]:
                max_list[2] = max_list[1]
                max_list[1] = nums[r]
            elif nums[r] > max_list[2]:
                max_list[2] = nums[r]

    print(max_list[0] if length_of_max_list != 3 else max_list[2])

    print(max_list)


def third_max_v3(nums: List[int]):
    max_list = [nums[0]]
    length_of_max_list = 1
    for r in range(1, len(nums)):
        if nums[r] in max_list:
            continue
        if length_of_max_list == 1:
            if nums[r] > max_list[0]:
                max_list.insert(0, nums[r])
            elif nums[r] < max_list[0]:
                max_list.append(nums[r])
            length_of_max_list += 1
        elif length_of_max_list == 2:
            if nums[r] > max_list[0]:
                max_list.insert(0, nums[r])
            elif nums[r] > max_list[1]:
                max_list.insert(1, nums[r])
            elif nums[r] < max_list[1]:
                max_list.append(nums[r])
            length_of_max_list += 1
        elif length_of_max_list == 3:
            if nums[r] > max_list[0]:
                max_list.insert(0, nums[r])
            elif nums[r] > max_list[1]:
                max_list.insert(1, nums[r])
            elif nums[r] > max_list[2]:
                max_list[2] = nums[r]

    print(max_list[0] if length_of_max_list != 3 else max_list[2])

    print(max_list)


def third_max(nums: List[int]):
    max_1 = (-1, False)
    max_2 = (-1, False)
    max_3 = (-1, False)
    for num in nums:
        if (max_1[1] and max_1[0] == num) or (max_2[1] and max_2[0] == num) or (max_3[1] and max_3[0] == num):
            continue
        if not max_1[1] or num > max_1[0]:
            max_3 = max_2
            max_2 = max_1
            max_1 = (num, True)
        elif not max_2[1] or num > max_2[0]:
            max_3 = max_2
            max_2 = (num, True)
        elif not max_3[1] or num > max_3[0]:
            max_3 = (num, True)
    print(max_1[0] if not max_3[1] else max_3[0])


third_max([3, 2, 1])
third_max([1, 2])
third_max([2, 2, 3, 1])
