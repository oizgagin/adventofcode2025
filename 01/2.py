import sys


def solve(moves):
    pos = 50

    D = {"L": -1, "R": 1}

    res = 0

    for dir_, clicks in moves:
        res += clicks // 100

        for c in range(clicks % 100):
            pos = (pos + D[dir_]) % 100
            if pos == 0: res += 1
    print(res)


def parse(it):
    for move in it.readlines():
        yield (move[0], int(move[1:]))


if __name__=="__main__": solve(parse(sys.stdin))
