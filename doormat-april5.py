# https://www.hackerrank.com/challenges/designer-door-mat/problem
# N is rows
# M is columns, and always 3x N
# N must be >= 5

"""
    Example:
    N is 9, M is 27

    Pattern learning:
    (i of N)
    (1 of 9) 12 - // 1 .|. // 12 -
    (2 of 9) 9 - // 3 .|. // 9 -
    (3 of 9) 6 - // 5 .|. // 6 -
    (4 of 9) 3 - // 7 .|. // 3 -
    (5 of 9) 10 - // WELCOME (7) // 10 -
    (6 of 9) 3 - // 7 .|. // 3 -
    (7 of 9) 6 - // 5 .|. // 6 -
    (8 of 9) 9 - // 3 .|. // 9 -
    (9 of 9) 12 - // 1 .|. // 12 -

"""
# from raw input formatting in hackerrank:
# N, M = map(int,raw_input().split(" "))

# formatting for running in terminal:
import sys
N = int(sys.argv[1])
M = 3 * N

# d is num of dashes
# v is num of .|.

for i in xrange(1, N + 1):

    if i <= N/2:
        v = (i*2) - 1
        d = (M - (3*v)) / 2
        center = v * ".|."

    elif i == N/2 + 1:
        d = ((M - 7) / 2)
        center = "WELCOME"

    elif i <= N:
        v = ((N - i)*2) + 1
        d = (M - (3*v)) / 2
        center = v * ".|."

    dashes = d * "-"
    print dashes + center + dashes
