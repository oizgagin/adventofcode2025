import heapq
from functools import reduce, cache
from itertools import product
import collections
import sys


def solve(args):
    figures, grids = args

    def _ok(grid):
        w, h, presents = grid
        return w * h >= 9 * sum(presents)

    grids = list(filter(_ok, grids))
    print(len(grids))


def parse(it):
    blocks = it.read().split("\n\n")

    figures = []
    for block in blocks[:-1]:
        figure = []
        for i, line in enumerate(block.splitlines()[1:]):
            for j, ch in enumerate(line):
                if ch == "#": figure.append((i, j))
        figures.append(tuple(figure))

    grids = []
    for line in blocks[-1].splitlines():
        dim, presents = tuple(line.split(":"))

        w, h = tuple(map(int, dim.split("x")))
        grids.append((w, h, tuple(map(int, presents.split()))))

    return figures, grids


if __name__=="__main__": solve(parse(sys.stdin))
