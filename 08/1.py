import heapq
from functools import reduce
from itertools import product
import collections
import sys


def solve(coords):

    def uf(n):
        p = list(range(n))
        c = [1] * n
        n = n

        def find(p1):
            if p[p1] != p1:
                p[p1] = find(p[p1])
            return p[p1]

        def union(p1, p2):
            pp1, pp2 = find(p1), find(p2)
            if pp1 != pp2:
                p[pp1] = pp2
                c[pp2] += c[pp1]
                return True
            return False

        def roots():
            for i in range(n):
                if find(i) == i:
                    yield i

        def size(p1):
            return c[find(p1)]

        return union, find, roots, size

    N = len(coords)

    d = lambda p1, p2: sum(map(lambda t: (t[0] - t[1]) ** 2, zip(p1, p2)))

    h = []

    for i in range(N):
        for j in range(i+1, N):
            heapq.heappush(h, (d(coords[i], coords[j]), i, j))

    union, find, roots, size = uf(N)

    for _ in range(1000):
        _, i, j = heapq.heappop(h)
        union(i, j)

    circuits = []
    for root in roots():
        circuits.append(size(root))

    circuits.sort(reverse=True)
    print(reduce(lambda acc, x: acc * x, circuits[:3], 1))


def parse(it):
    coords = []
    for line in it.readlines():
        coords.append(tuple(map(int, line.split(","))))
    return coords


if __name__=="__main__": solve(parse(sys.stdin))
