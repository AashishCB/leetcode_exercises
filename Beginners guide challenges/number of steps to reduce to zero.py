def number_of_steps_v1(num: int):
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num = num//2
        else:
            num -= 1
        steps += 1
    print(steps)


def number_of_steps(num: int):
    steps = 0
    while num > 0:
        if num & 1 == 0:
            num >>= 1
        else:
            num -= 1
        steps += 1


number_of_steps(14)
number_of_steps(8)
number_of_steps(123)
