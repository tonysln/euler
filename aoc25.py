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


def day3_p2(fpath):
    """
    https://adventofcode.com/2025/day/3#part2
    """

    with open(fpath, "r") as f:
        lines = f.read().strip().splitlines()

    lines = """987654321111111
811111111111119
234234234234278
818181911112111""".strip().split("\n")

    total = 0

    for bank in lines:
        print(bank)

    return total


def day4_p1(fpath):
    """
    https://adventofcode.com/2025/day/4
    """
    return None


def day4_p2(fpath):
    """
    https://adventofcode.com/2025/day/4#part2
    """
    return None


def day5_p1(fpath):
    """
    https://adventofcode.com/2025/day/5
    """

    with open(fpath, "r") as f:
        lines = f.read().strip().splitlines()

    spl = lines.index('')
    ranges = []
    for i in range(0, spl):
        ranges.append(tuple(map(int, lines[i].split('-', 1))))

    pts = []
    for i in range(spl+1, len(lines)):
        pts.append(int(lines[i]))

    srng = sorted(ranges)
    spts = sorted(pts)

    i = 0
    j = 0
    ctr = 0
    while i < len(srng) and j < len(spts):
        pt = spts[j]
        start,end = srng[i]
        
        if pt > end:
            i += 1
            continue
        
        if pt >= start and pt <= end:
            ctr += 1

        j += 1

    return ctr


def day5_p2(fpath):
    """
    https://adventofcode.com/2025/day/5#part2
    """

    with open(fpath, "r") as f:
        lines = f.read().strip().splitlines()

    spl = lines.index('')
    ranges = []
    for i in range(0, spl):
        ranges.append(tuple(map(int, lines[i].split('-', 1))))

    srng = sorted(ranges)
    nrng = [[srng[0][0],srng[0][1]]]
    i = 1
    while i < len(srng):
        li = len(nrng)-1
        cs,ce = srng[i]
        if cs <= nrng[li][1]:
            nrng[li][1] = max(ce,nrng[li][1])
        else:
            nrng.append([cs,ce])

        i += 1
    
    # print('===')
    print(nrng)
    ctr = sum([el[1]-el[0]+1 for el in nrng])

    return ctr


def day6_p1(fpath):
    """
    https://adventofcode.com/2025/day/6
    """

    with open(fpath, "r") as f:
        data = [line.split() for line in f.read().splitlines()]

    vals = [list(map(int, row)) for row in data[:-1]]
    ops = data[-1]

    ans = []
    for i in range(len(ops)):
        ans.append(vals[0][i])

        for j in range(1, len(vals)):
            if ops[i] == '+':
                ans[-1] += vals[j][i]
            else:
                ans[-1] *= vals[j][i]

    return sum(ans)


def day6_p2(fpath):
    """
    https://adventofcode.com/2025/day/6#part2
    """

    with open(fpath, "r") as f:
        data = [line.split() for line in f.read().splitlines()]

    return None


def day7_p1(fpath):
    """
    https://adventofcode.com/2025/day/7
    """
    return None


def day7_p2(fpath):
    """
    https://adventofcode.com/2025/day/7#part2
    """
    return None


def day8_p1(fpath):
    """
    https://adventofcode.com/2025/day/8
    """
    return None


def day8_p2(fpath):
    """
    https://adventofcode.com/2025/day/8#part2
    """
    return None


def day9_p1(fpath):
    """
    https://adventofcode.com/2025/day/9
    """
    return None


def day9_p2(fpath):
    """
    https://adventofcode.com/2025/day/9#part2
    """
    return None


def day10_p1(fpath):
    """
    https://adventofcode.com/2025/day/10
    """
    return None


def day10_p2(fpath):
    """
    https://adventofcode.com/2025/day/10#part2
    """
    return None


def day11_p1(fpath):
    """
    https://adventofcode.com/2025/day/11
    """
    return None


def day11_p2(fpath):
    """
    https://adventofcode.com/2025/day/11#part2
    """
    return None


def day12_p1(fpath):
    """
    https://adventofcode.com/2025/day/12
    """
    return None


def day12_p2(fpath):
    """
    https://adventofcode.com/2025/day/12#part2
    """
    return None


if __name__ == "__main__":
    # print("D1_P1:", day1_p1("day1.txt"))
    # print("D1_P2:", day1_p2("day1.txt"))
    # print("D2_P1:", day2_p1("day2.txt"))
    # print("D2_P2:", day2_p2("day2.txt"))
    # print("D3_P1:", day3_p1("day3.txt"))
    # print("D3_P2:", day3_p2("day3.txt"))
    # print("D4_P1:", day4_p1("day4.txt"))
    # print("D4_P2:", day4_p2("day4.txt"))
    # print("D5_P1:", day5_p1("day5.txt"))
    # print("D5_P2:", day5_p2("day5.txt"))
    print("D6_P1:", day6_p1("day6.txt"))
    # print("D6_P2:", day6_p2("day6.txt"))
    # print("D7_P1:", day7_p1("day7.txt"))
    # print("D7_P2:", day7_p2("day7.txt"))
    # print("D8_P1:", day8_p1("day8.txt"))
    # print("D8_P2:", day8_p2("day8.txt"))
    # print("D9_P1:", day9_p1("day9.txt"))
    # print("D9_P2:", day9_p2("day9.txt"))
    # print("D10_P1:", day10_p1("day10.txt"))
    # print("D10_P2:", day10_p2("day10.txt"))
    # print("D11_P1:", day11_p1("day11.txt"))
    # print("D11_P2:", day11_p2("day11.txt"))
    # print("D12_P1:", day12_p1("day12.txt"))
    # print("D12_P2:", day12_p2("day12.txt"))
