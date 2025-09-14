#! /usr/bin/python3

from functools import wraps
import time
import math


def is_odd(n):
    return n & 1

def timed(f):
    @wraps(f)
    def timed_wrapper(*args, **kwargs):
        a = time.monotonic()
        res = f(*args, **kwargs)
        b = time.monotonic()
        print(f'{round(b-a, 4)}s')
        return res

    return timed_wrapper


def collatz_count(n, d, limit=1e10):
    c = 1
    nn = n
    while n > 1 and c < limit:
        if n in d:
            return c + d[n]
        else:
            n = (3*n + 1) if n & 1 else (n // 2)
            if n == 1:
                d[nn] = c
                return d[nn]
        c += 1

    d[nn] = c
    return d[nn]


@timed
def problem_1(N=1e4):
    """
    Multiples of 3 or 5
    Problem 1
    """
    s = 0
    for i in range(1, int(N)):
        if i % 3 == 0 or i % 5 == 0:
            s += i

    return s


@timed
def problem_4(d=3):
    """
    Largest Palindrome Product
    Problem 4
    """
    pmax = (-1, -1, -1)
    for a in range(10**(d-1), 10**d):
        for b in range(10**(d-1), 10**d):
            if b <= a:
                continue

            p = a * b
            if str(p) == str(p)[::-1]:
                if p > pmax[0]:
                    pmax = (p, a, b)

    return pmax


@timed
def problem_14(N=1e6):
    """
    Longest Collatz Sequence
    Problem 14
    """
    m = -1
    mn = -1
    d = {}
    for n in range(int(N)-1, -1, -1):
        c = collatz_count(n, d)
        if c > m:
            m = c
            mn = n

    return mn,m


@timed
def problem_28(side):
    """
    Number Spiral Diagonals
    Problem 28
    """
    n = side*side
    i = round(math.sqrt(n))
    s = 0
    while i >= 1:
        s += sum(set([n, n-i+1, n-i*2+2, n-i*3+3]))
        i -= 2
        n = i*i

    return s


if __name__ == '__main__':
    print('* Problem 1:\n', problem_1(1e4))
    print('* Problem 4:\n', problem_4(3))
    print('* Problem 14:\n', problem_14(1e5))
    print('* Problem 28:\n', problem_28(1001))



