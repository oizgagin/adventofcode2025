import heapq
from functools import reduce
from itertools import product
import collections
import sys


def solve(coords):
    N = len(coords)

    area = lambda c1, c2: (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)

    v, h = [], []
    for i in range(N):
        c1, c2 = coords[i], coords[(i-1)%N]

        if c1[0] == c2[0]:
            v.append((c1[0], min(c1[1], c2[1]), max(c1[1], c2[1])))
        else:
            assert c1[1] == c2[1]
            h.append((c1[1], min(c1[0], c2[0]), max(c1[0], c2[0])))

    v.sort()
    h.sort()

    maxls = []
    for y, x1, x2 in h:
        maxls.append((x2 - x1, y, x1, x2))
    maxls.sort(reverse=True)

    ylow = min(maxls[0][1], maxls[1][1])
    yhigh = max(maxls[0][1], maxls[1][1])

    res = float('-inf')
    for c1 in coords:
        for c2 in coords:
            if c1 == c2: continue

            x1, y1 = c1
            x2, y2 = c2

            minx, maxx = min(x1, x2), max(x1, x2)
            miny, maxy = min(y1, y2), max(y1, y2)

            if (miny < ylow < maxy or miny < yhigh < maxy):
                continue

            x1, y1 = minx + 0.5, miny + 0.5
            x2, y2 = maxx - 0.5, maxy - 0.5

            c = 0
            for vx, vy1, vy2 in v:
                if vx > x1 and vy1 < y1 < vy2:
                    c += 1
            if c % 2 == 0:
                continue

            c = 0
            for vx, vy1, vy2 in v:
                if vx > x2 and vy1 < y2 < vy2:
                    c += 1
            if c % 2 == 0:
                continue

            x3, y3 = minx + 0.5, maxy - 0.5
            x4, y4 = maxx - 0.5, miny + 0.5

            c = 0
            for vx, vy1, vy2 in v:
                if vx > x3 and vy1 < y3 < vy2:
                    c += 1
            if c % 2 == 0:
                continue

            c = 0
            for vx, vy1, vy2 in v:
                if vx > x4 and vy1 < y4 < vy2:
                    c += 1
            if c % 2 == 0:
                continue

            res = max(res, area(c1, c2))

    print(res)


def parse(it):
    coords = []
    for line in it.readlines():
        coords.append(tuple(map(int, line.split(","))))
    return coords


if __name__=="__main__": solve(parse(sys.stdin))
