from itertools import product
import sys


def solve(t):
    intervals, ingredients = t

    fresh = 0
    for ingredient in ingredients:
        for a, b in intervals:
            if a <= ingredient <= b:
                fresh += 1
                break
    print(fresh)


def parse(it):
    intervals, ingredients = it.read().split("\n\n")

    intervals = list(map(lambda l: tuple(map(int, l.split('-'))), intervals.splitlines()))
    ingredients = list(map(int, ingredients.splitlines()))

    return intervals, ingredients


if __name__=="__main__": solve(parse(sys.stdin))
