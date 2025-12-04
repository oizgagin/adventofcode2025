from itertools import product
import sys


def solve(grid):
    R, C = len(grid), len(grid[0])

    in_ = lambda r, c: 0 <= r < R and 0 <= c < C

    def neighs(r, c):
        D = (-1, 0, 1)
        for dr, dc in product(D, D):
            if dr == dc == 0: continue
            if in_(r+dr, c+dc): yield (r+dr, c+dc)

    res = 0

    while True:
        removed = False

        for r, c in product(range(R), range(C)):
            if grid[r][c] == '.': continue

            ns = 0
            for nr, nc in neighs(r, c):
                if grid[nr][nc] == '@': ns += 1

            if ns < 4:
                removed = True
                grid[r][c] = '.'
                res += 1

        if not removed:
            break

    print(res)


def parse(it):
    return [ list(s.strip()) for s in it.readlines() ]


if __name__=="__main__": solve(parse(sys.stdin))
