"""Test problem setup uses os and sys; that has been commented out to 
prevent file issues. """

#!/bin/python

# from __future__ import print_function

# import os
# import sys

#
# Complete the diagonalDifference function below.
#

def diagonalDifference(a):

    # a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    # first, previous + 1, previous + 1
    # last, previous - 1, previous - 1

    primary_sum = 0
    secondary_sum = 0
    current = 0

    for row in a:
    # for each sublist

        primary_sum += row[current]
        if current < len(row) - 1:
        # all rows are the same length. This control constraint stops adding one after the last row
            current += 1

    for row in a:

        secondary_sum += row[current]
        current -= 1

    return abs(primary_sum - secondary_sum)


a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print diagonalDifference(a)


# if __name__ == '__main__':
#     f = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(raw_input())

#     a = []

#     for _ in xrange(n):
#         a.append(map(int, raw_input().rstrip().split()))

#     result = diagonalDifference(a)

#     f.write(str(result) + '\n')

#     f.close()