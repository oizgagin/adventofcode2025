from functools import reduce
from itertools import product
import collections
import sys


def solve(grid):
    R, C = len(grid), len(grid[0])

    i, j = 0, grid[0].index('S')

    res = 0

    seen = set()

    q = collections.deque([(0, j)])
    while len(q) > 0:
        for _ in range(len(q)):
            i, j = q.popleft()

            if (i, j) in seen:
                continue

            seen.add((i, j))

            if i+1 < R:
                if grid[i+1][j] == '^':
                    res += 1
                    if 0 <= j-1:
                        q.append((i+1, j-1))
                    if j+1 < C:
                        q.append((i+1, j+1))
                else:
                    q.append((i+1, j))
    print(res)


def parse(it):
    return list(map(str.strip, it.readlines()))


if __name__=="__main__": solve(parse(sys.stdin))
