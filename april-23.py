

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

