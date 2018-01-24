# !/usr/bin/python

from bootstrap import *
from raspledstrip.animation import *

n = 10 # number of times to scan

#scanner: single color and changing color
anim = LarsonScanner(led, Color(0, 0, 255)) ## Blue
for i in range(led.last_index * n):
    anim.step()
    led.update()
#sleep(0.03)

#led.fill_off()

led.all_off()

