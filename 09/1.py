import heapq
from functools import reduce
from itertools import product
import collections
import sys


def solve(coords):

    area = lambda c1, c2: abs(c1[0] - c2[0] + 1) * abs(c1[1] - c2[1] + 1)

    res = float('-inf')
    for c1 in coords:
        for c2 in coords:
            if c1 != c2:
                res = max(res, area(c1, c2))
    print(res)


def parse(it):
    coords = []
    for line in it.readlines():
        coords.append(tuple(map(int, line.split(","))))
    return coords


if __name__=="__main__": solve(parse(sys.stdin))
