import heapq
from functools import reduce, cache
from itertools import product
import collections
import sys


def solve(g):

    @cache
    def recurse(node, end, exclude):
        if node == end:
            return 1

        res = 0
        for neigh in g[node]:
            if neigh not in exclude:
                res += recurse(neigh, end, exclude)
        return res

    v1 = recurse("svr", "fft", ("dac", "out"))
    v2 = recurse("svr", "dac", ("fft", "out"))
    v3 = recurse("fft", "dac", ("svr", "out"))
    v4 = recurse("dac", "fft", ("svr", "out"))
    v5 = recurse("fft", "out", ("svr", "dac"))
    v6 = recurse("dac", "out", ("svr", "fft"))

    # svr -> fft -> dac -> out
    v7 = v1 * v3 * v6

    # svr -> dac -> fft -> out
    v8 = v2 * v4 * v5

    print(v7 + v8)


def parse(it):
    g = collections.defaultdict(list)

    for line in it.readlines():
        from_, tos = line.split(":")
        for to in tos.split():
            g[from_].append(to)
    return g


if __name__=="__main__": solve(parse(sys.stdin))
