from itertools import combinations
from math import factorial


def main():
    deck = [i for _ in range(4) for i in range(1, 15)]
    ans = 0
    for elem in combinations(deck, 6):
        ans += sum(elem) == 21
    print(ans * factorial(46) * factorial(6) / factorial(52))

main()
