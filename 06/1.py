from functools import reduce
from itertools import product
import sys


def solve(args):
    numbers, ops = args

    res = 0
    for i in range(len(numbers[0])):

        op = ops[i]

        if op == '*':
            res += reduce(lambda acc, x: acc * x, map(lambda row: row[i], numbers), 1)
        else:
            assert op == '+'
            res += reduce(lambda acc, x: acc + x, map(lambda row: row[i], numbers), 0)

    print(res)


def parse(it):
    lines = it.readlines()

    numbers = list(map(lambda line: tuple(map(int, line.split())), lines[:-1]))
    ops = lines[-1].strip().split()

    return numbers, ops


if __name__=="__main__": solve(parse(sys.stdin))
