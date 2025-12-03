#! /usr/bin/python3


def day1_p1(fpath):
    """
    https://adventofcode.com/2025/day/1
    """

    with open(fpath, "r") as f:
        lines = f.read().splitlines()

    dial = 50
    zd = 0

    for rot in lines:
        val = int(rot[1:])

        if rot[0] == "L":
            val *= -1

        dial = (dial + val) % 100
        if dial == 0:
            zd += 1

    return zd


def day1_p2(fpath):
    """
    https://adventofcode.com/2025/day/1#part2
    """
    with open(fpath, "r") as f:
        lines = f.read().splitlines()

    dial = 50
    zd = 0

    for rot in lines:
        val = int(rot[1:])

        mult = -1 if rot[0] == "L" else 1

        for _ in range(0, val):
            if dial == 0:
                zd += 1

            dial = (dial + mult) % 100

    return zd


def day2_p1(fpath):
    """
    https://adventofcode.com/2025/day/2
    """
    with open(fpath, "r") as f:
        ranges = f.read().strip().split(",")

    sum = 0

    for r in ranges:
        r = r.split("-")
        v1 = int(r[0])
        v2 = int(r[1])

        for v in range(v1, v2 + 1):
            sv = str(v)
            for i in range(1, len(sv) // 2 + 1):
                if sv[:i] * 2 == sv:
                    sum += v

    return sum


def day2_p2(fpath):
    """
    https://adventofcode.com/2025/day/2#part2
    """
    with open(fpath, "r") as f:
        ranges = f.read().strip().split(",")

    sum = 0

    for r in ranges:
        r = r.split("-")
        v1 = int(r[0])
        v2 = int(r[1])

        for v in range(v1, v2 + 1):
            sv = str(v)
            for i in range(1, len(sv) // 2 + 1):
                if sv.count(sv[:i]) * i == len(sv):
                    sum += v
                    break

    return sum


def day3_p1(fpath):
    """
    https://adventofcode.com/2025/day/3
    """
    with open(fpath, "r") as f:
        lines = f.read().strip().splitlines()

    total = 0

    for bank in lines:
        ibank = [(int(e), i) for i, e in enumerate(bank)]
        sbank = sorted(ibank, key=lambda x: x[0], reverse=True)

        best = 0
        # not nice but good enough
        for i in range(0, len(bank)):
            for j in range(0, len(bank)):
                if i == j:
                    continue

                a = sbank[i]
                b = sbank[j]
                if a[1] < b[1]:
                    continue

                c = int(f"{b[0]}{a[0]}")
                if c > best:
                    best = c

        total += best

    return total


if __name__ == "__main__":
    # print("D1_P1:", day1_p1("day1.txt"))
    # print("D1_P2:", day1_p2("day1.txt"))
    # print("D2_P1:", day2_p1("day2.txt"))
    # print("D2_P2:", day2_p2("day2.txt"))
    print("D3_P1:", day3_p1("day3.txt"))
