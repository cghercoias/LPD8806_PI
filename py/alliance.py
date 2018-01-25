#!/usr/bin/python

from bootstrap import *
from raspledstrip.animation import *
#Alliance = A
B = 1
R = 2
A = 1
if (A == 1):
	colors = [
#    (255.0, 0.0, 0.0),         # red
    (0.0, 255.0, 0.0),          # blue
#    (0.0, 0.0, 255.0),         # green
]

n = 1 # how many colors to light up

step = 0.01
for c in range(n):
    r, g, b = colors[c]
    level = 0.01
    dir = step
    while level >= 0.0:
        led.fill(Color(r, g, b, level))
        led.update()
        if (level >= 0.99):
            dir = -step
        level += dir
if (A == 2):
	led.all_off()
	colors = [  
  (255.0, 0.0, 0.0),         # red
#    (0.0, 255.0, 0.0),          # blue
#    (0.0, 0.0, 255.0),         # green
]

n = 1 # how many colors to light up

step = 0.01
for c in range(n):
    r, g, b = colors[c]
    level = 0.01
    dir = step
    while level >= 0.0:
        led.fill(Color(r, g, b, level))
        led.update()
        if (level >= 0.99):
            dir = -step
        level += dir
   















