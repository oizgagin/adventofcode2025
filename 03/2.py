from functools import cache
import sys


def solve(banks):

    @cache
    def dp(bank, i, left):
        if i >= len(bank):
            return float('-inf')

        if left == 1:
            return max(bank[i:])

        return max(
            bank[i] * (10 ** (left - 1)) + dp(bank, i+1, left-1),
            dp(bank, i+1, left)
        )

    res = 0
    for bank in banks:
        res += dp(bank, 0, 12)
    print(res)


def parse(it):
    return [ tuple(map(int, s.strip())) for s in it.readlines() ]


if __name__=="__main__": solve(parse(sys.stdin))
