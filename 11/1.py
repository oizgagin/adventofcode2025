import heapq
from functools import reduce, cache
from itertools import product
import collections
import sys


def solve(g):

    def recurse(node):
        if node == "out":
            return 1

        res = 0
        for neigh in g[node]:
            res += recurse(neigh)
        return res

    print(recurse("you"))


def parse(it):
    g = collections.defaultdict(list)

    for line in it.readlines():
        from_, tos = line.split(":")
        for to in tos.split():
            g[from_].append(to)
    return g


if __name__=="__main__": solve(parse(sys.stdin))
