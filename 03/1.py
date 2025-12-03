import sys


def solve(banks):
    res = 0
    for bank in banks:
        v = float('-inf')
        for i in range(len(bank)):
            for j in range(i+1, len(bank)):
                v = max(v, bank[i] * 10 + bank[j])
        res += v
    print(res)


def parse(it):
    return [ list(map(int, s.strip())) for s in it.readlines() ]


if __name__=="__main__": solve(parse(sys.stdin))
