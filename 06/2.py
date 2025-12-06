from functools import reduce
from itertools import product
import sys


def solve(args):
    numbers, ops, lines = args

    res = 0

    for i in range(len(numbers[0])):
        width = max([len(str(row[i])) for row in numbers])

        col = []
        for j in range(len(lines)):
            col.append(lines[j][:width])
            lines[j] = lines[j][width+1:]

        op = ops[i]

        if op == '*':
            acc = 1
            op = lambda acc, x: acc * x
        else:
            acc = 0
            op = lambda acc, x: acc + x

        for c in range(width):
            curr = 0
            for l in col:
                if l[c] == ' ': continue
                curr = curr * 10 + int(l[c])
            acc = op(acc, curr)

        res += acc

    print(res)


def parse(it):
    lines = it.readlines()

    numbers = list(map(lambda line: tuple(map(int, line.split())), lines[:-1]))
    ops = lines[-1].strip().split()

    return numbers, ops, lines[:-1]


if __name__=="__main__": solve(parse(sys.stdin))
