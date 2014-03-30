#!/usr/bin/python

import math
everything = dir(math)
print everything

def distance_from_zero(num):
    if type(num) == int or type(num) == float:
        return abs(num)
    else:
        return 'Nope'