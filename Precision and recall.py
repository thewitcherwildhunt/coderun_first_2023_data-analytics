import re


def coincidence(line):
    pass


def main():
    n, k = map(int, input().split())
    TP, TN, FP, FN = 0, 0, 0, 0
    for _ in range(n):
        if coincidence(input()):
            print('ok')
            TP += 1
        else:
            FN += 1
    for _ in range(k):
        if coincidence(input()):
            print('ok')
            FP += 1
        else:
            TN += 1
    print(TP, TN, FP, FN)
    print(TP / (TP + FN), TP / (FP + TP))

main()
