# y = A * sin(2*pi*f*t)
#radian * 180/pi = degree

from math import pi, sin
from sys import stdin

config = list()

for line in stdin:
    config.append(line)


"""
======= VERIFICATION CONFIG FILE, ASSIGNING VARIABLES =======
"""
if config[0].split('=')[0].strip().lower() == 'frequency':
    FREQUENCY = int(config[0].split('=')[1].strip())
else:
    print('Expected: Frequency. Recieved : {}'.format(config[0].split('=')[0].strip()))

if config[1].split('=')[0].strip().lower() == 'time':
    TIME = int(config[1].split('=')[1].strip())
else:
    print('Expected: Time. Recieved : {}'.format(config[1].split('=')[0].strip()))

if config[2].split('=')[0].strip().lower() == 'amplitude':
    AMPLITUDE = int(config[2].split('=')[1].strip())
else:
    print('Expected: Amplitude. Recieved : {}'.format(config[2].split('=')[0].strip()))

try:
    print(FREQUENCY, TIME, AMPLITUDE)
except Exception as e: 
    print(e)