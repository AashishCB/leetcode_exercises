def fizz_buzz_v1(n: int):
    answer = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
    print(answer)


def fizz_buzz(n: int):
    answer = []
    for i in range(1, n+1):
        answer_string = ""
        if i % 3 == 0:
            answer_string += "Fizz"
        if i % 5 == 0:
            answer_string += "Buzz"
        if not answer_string:
            answer_string += str(i)
        answer.append(answer_string)
    print(answer)


fizz_buzz(3)
fizz_buzz(5)
fizz_buzz(15)
