#! /usr/bin/python3

from functools import wraps, lru_cache
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


def primes_up_to(n):
    A = [False] + [True]*n
    
    for i in range(2, math.ceil(math.sqrt(n))):
        if A[i]:
            isq = i*i
            j = isq
            f = 1
            while j <= n:
                A[j] = False
                j = isq + f*i
                f += 1
                
    return list(filter(lambda i: A[i], range(2, len(A))))


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


@lru_cache
def fibonacci(n):
    return fibonacci(n-1) + fibonacci(n-2) if n > 2 else n


@timed
def problem_2(N=1e6):
    """
    Even Fibonacci Numbers
    Problem 2
    """
    s = 0
    i = 2
    while True:
        n = fibonacci(i)
        if n > N:
            break
        s += n
        i += 3
    return s


@timed
def problem_3(n):
    """
    Largest Prime Factor
    Problem 3
    """
    P = primes_up_to(int(math.sqrt(n)))
    f = []

    for p in P:
        while n % p == 0:
            f.append(int(p))
            n /= p

    if n > 1:
        f.append(int(n))

    return max(f)


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
def problem_6(N=1e3):
    """
    Sum Square Difference
    Problem 6
    """
    s1 = 0
    s2 = 0
    for i in range(1, int(N)+1):
        s1 += i*i
        s2 += i

    return s2*s2 - s1


@timed
def problem_10(N=1e6):
    """
    Summation of Primes
    Problem 10
    """
    return sum(primes_up_to(int(N)))


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
def problem_25(N=1e3):
    """
    1000-digit Fibonacci Number
    Problem 25
    """
    i = 1
    while True:
        n = fibonacci(i)
        if math.floor(math.log10(n))+1 == int(N):
            return i+1

        i += 1

    return -1


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


def rotations(n, primes):
    c = set()
    for i in range(int(len(str(n)))+1):
        c.add(n)

        n = int(str(n)[-1] + str(n)[0:-1])
        if n not in primes: 
            return set()
            
    return c


@timed
def problem_35(N=100):
    """
    Circular Primes
    Problem 35
    """
    P = primes_up_to(int(N))
    cprimes = []
    for p in P:
        c = rotations(p, P)
        if c:
            cprimes.append(c)

    return len(cprimes), cprimes


def bouncy(n):
    c = [True, True]
    
    p = n % 10
    n = n // 10
    while n:
        d = n % 10

        if d > p: # inc
            c[0] = False
            if not c[1]: return True
        
        if d < p: # dec
            c[1] = False
            if not c[0]: return True

        p = d
        n = n // 10

    return not sum(c)


@timed
def problem_112(p=0.5):
    """
    Bouncy Numbers
    Problem 112
    """
    b = 0
    n = 1
    while True:
        if bouncy(n):
            b += 1

        if b / n >= p:
            return n

        n += 1

    return -1


if __name__ == '__main__':
    # print('* Problem 1:\n', problem_1(1e4))
    # print('* Problem 2:\n', problem_2(4e6))
    # print('* Problem 3:\n', problem_3(13195))
    # print('* Problem 3:\n', problem_3(600851475143))
    # print('* Problem 4:\n', problem_4(3))
    # print('* Problem 6:\n', problem_6(100))
    # print('* Problem 10:\n', problem_10(2e6))
    # print('* Problem 14:\n', problem_14(1e5))
    # print('* Problem 25:\n', problem_25(1e3))
    # print('* Problem 28:\n', problem_28(1001))
    # print('* Problem 35:\n', problem_35(1e5))
    # print('* Problem 112:\n', problem_112(0.5))
    print('* Problem 112:\n', problem_112(0.99))

 