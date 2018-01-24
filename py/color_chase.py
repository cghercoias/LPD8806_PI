# !/usr/bin/python

from bootstrap import *
from raspledstrip.animation import *

#setup colors to loop through for fade
colors = [
    (255.0, 0.0, 0.0),
   # (0.0, 255.0, 0.0),
   # (0.0, 0.0, 255.0),
    (255.0, 255.0, 255.0),
]
led_count = 48
n =2 # how many colors to lit up

#step = 0.01
#for c in range(n):
#    r, g, b = colors[c]
#    level = 0.01
#    dir = step
#    while level >= 0.0:
#        led.fill(Color(r, g, b, level))
#        led.update()
#        if (level >= 0.99):
#            dir = -step
#        level += dir
#sleep(0.005)


for c in range(n):
    anim = ColorChase(led, colors[c])

    for i in range(led_count):
        anim.step()
        led.update()
    #sleep(0.03)

led.all_off()


