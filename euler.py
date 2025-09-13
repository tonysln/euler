#! /usr/bin/python3

from functools import wraps
import time


def is_odd(n):
	return n & 1


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


def timed(f):
	@wraps(f)
	def timed_wrapper(*args, **kwargs):
		a = time.monotonic()
		res = f(*args, **kwargs)
		b = time.monotonic()
		print(f'{round(b-a, 4)}s')
		return res

	return timed_wrapper


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

	return m,mn


print('* Problem 14:')
print(problem_14(1e6))
