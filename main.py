# y = A * sin(2*pi*f*t)
#radian * 180/pi = degree

from math import exp, pi, sin
from sys import stdin
from modules import *


config = list()

for line in stdin:
    config.append(line)

"""
======= VERIFICATION CONFIG FILE, ASSIGNING VARIABLES =======
"""
try:
    res = verification(config, 'frequency', 'time', 'amplitude')
    FREQUENCY,TIME,AMPLITUDE = res 
    print(FREQUENCY,TIME,AMPLITUDE)
except ValueError:
    print('There are some errors in config File. Not enough values to unpack (expected 3, got {})'.format(len(res)))

# not enough values to unpack (expected 3, got 0)