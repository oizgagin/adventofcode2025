import heapq
from functools import reduce, cache
from itertools import product
import collections
import sys


def solve(it):
    res = 0

    for light, buttons in it:
        best = float('inf')
        for m in range(1 << len(buttons)):
            curr = ops = 0

            for i in range(1 << len(buttons)):
                if m & (1 << i):
                    curr ^= buttons[i]
                    ops += 1

            if curr == light:
                best = min(best, ops)

        res += best

    print(res)


def parse(it):
    for line in it.readlines():
        s = line.split()

        light = 0
        for i, ch in enumerate(s[0].strip('[]')):
            if ch == '#': light |= (1 << i)

        buttons = []
        for button in s[1:-1]:
            buttons.append(sum(map(lambda v: 1 << int(v), button.strip('()').split(','))))

        yield light, buttons


if __name__=="__main__": solve(parse(sys.stdin))
