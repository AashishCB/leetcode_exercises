from typing import List


def maximum_wealth(accounts: List[List[int]]):
    wealth = 0
    for amounts in accounts:
        if sum(amounts) > wealth:
            wealth = sum(amounts)
    print(wealth)


maximum_wealth([[1, 2, 3], [3, 2, 1]])
maximum_wealth([[1, 5], [7, 3], [3, 5]])
maximum_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]])
