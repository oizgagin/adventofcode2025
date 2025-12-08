import heapq
from functools import reduce
from itertools import product
import collections
import sys


def solve(coords):

    def uf(n):
        p = list(range(n))
        c = n
        n = n

        def find(p1):
            if p[p1] != p1:
                p[p1] = find(p[p1])
            return p[p1]

        def union(p1, p2):
            nonlocal c

            pp1, pp2 = find(p1), find(p2)
            if pp1 != pp2:
                p[pp1] = pp2
                c -= 1
                return True
            return False

        def components():
            nonlocal c
            return c

        return union, find, components

    N = len(coords)

    d = lambda p1, p2: sum(map(lambda t: (t[0] - t[1]) ** 2, zip(p1, p2)))

    h = []

    for i in range(N):
        for j in range(i+1, N):
            heapq.heappush(h, (d(coords[i], coords[j]), i, j))

    union, find, components = uf(N)

    while True:
        _, i, j = heapq.heappop(h)
        union(i, j)
        if components() == 1:
            print(coords[i][0] * coords[j][0])
            return


def parse(it):
    coords = []
    for line in it.readlines():
        coords.append(tuple(map(int, line.split(","))))
    return coords


if __name__=="__main__": solve(parse(sys.stdin))
