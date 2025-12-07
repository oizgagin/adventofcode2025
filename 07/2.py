from functools import reduce, cache
from itertools import product
import collections
import sys


def solve(grid):
    R, C = len(grid), len(grid[0])

    i, j = 0, grid[0].index('S')


    @cache
    def solve(i, j):
        if not 0 <= j < C:
            return 0

        if i == R:
            return 1

        if grid[i][j] == '.' or grid[i][j] == 'S':
            return solve(i+1, j)

        return solve(i+1, j-1) + solve(i+1, j+1)

    print(solve(i, j))


def parse(it):
    return list(map(str.strip, it.readlines()))


if __name__=="__main__": solve(parse(sys.stdin))
