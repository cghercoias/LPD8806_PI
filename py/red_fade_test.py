# !/usr/bin/python

from bootstrap import *
from raspledstrip.animation import *

#setup colors to loop through for fade
colors = [
    (255.0, 0.0, 0.0), 		# red
#    (0.0, 255.0, 0.0), 		# blue
#    (0.0, 0.0, 255.0), 		# green
#    (255.0, 255.0, 255.0), 	# white
]

n = 1 # how many colors to lit up

step = 0.01
for c in range(n):
    r, g, b = colors[c]
    level = .1
    dir = step
    while level >= 0.0:
        led.fill(Color(r, g, b, level))
        led.update()
        if (level >= 0.99):
            dir = -step
        level += dir
    #sleep(0.005)

led.all_off()


