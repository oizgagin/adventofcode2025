import sys


def solve(it):
    res = 0
    for a, b in it:
        for c in range(a, b+1):
            s = str(c)
            if len(s) % 2 != 0:
                continue

            if s[:len(s)//2] == s[len(s)//2:]:
                res += c
    print(res)


def parse(it):
    _p = lambda r: tuple(map(int, r.split("-")))
    for r in it.readline().split(","):
        yield _p(r)


if __name__=="__main__": solve(parse(sys.stdin))
