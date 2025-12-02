#! /usr/bin/python3


def day1_p1(fpath):
	"""
	https://adventofcode.com/2025/day/1
	"""

	with open(fpath, 'r') as f:
		lines = f.read().splitlines()

	dial = 50
	zd = 0

	for rot in lines:
		val = int(rot[1:])

		if rot[0] == 'L':
			val *= -1

		dial = (dial + val) % 100
		if dial == 0:
			zd += 1

	return zd


if __name__ == '__main__':
	print('D1_P1:', day1_p1('day1.txt'))
