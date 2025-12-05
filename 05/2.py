from itertools import product
import sys


def solve(t):
    intervals, ingredients = t

    intervals.sort()

    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        a, b = intervals[i]

        if a <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], b)
        else:
            merged.append([a, b])

    res = 0
    for a, b in merged:
        res += b - a + 1
    print(res)


def parse(it):
    intervals, ingredients = it.read().split("\n\n")

    intervals = list(map(lambda l: list(map(int, l.split('-'))), intervals.splitlines()))
    ingredients = list(map(int, ingredients.splitlines()))

    return intervals, ingredients


if __name__=="__main__": solve(parse(sys.stdin))
