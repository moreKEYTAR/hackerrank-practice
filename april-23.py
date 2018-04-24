

#!/bin/python

# from __future__ import print_function

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):

    for i in xrange(len(grades)):
        if grades[i] >= 38:
            # using mod will determine if the value is closer to the lower multiple of 5 or higher:
            if grades[i] % 5 >= 3:
                rounded_grade = ((grades[i] / 5) + 1) * 5
                grades[i] =  rounded_grade
    return grades

#------------------------------------------#

def kangaroo(x1, v1, x2, v2):
    """Return a string YES or NO, denoting whether the two kangaroos will ever meet.
    Values for x denote the starting location on the number line, O or higher.
    Values for v denote the distance per second for that kangaroo."""
    # 0 3 4 2
    
    if v2 >= v1:  # We know x1 is always less than x2, so a faster x2 kangaroo means they will never meet
        return "NO"
    else:
        d1 = x1
        d2 = x2
        t = 0
        
        while d1 < d2:
            t += 1  # good thing to track, in case it is needed in a real use case
            d1 += v1
            d2 += v2
            if d1 == d2:
                return "YES"
    
    return "NO"