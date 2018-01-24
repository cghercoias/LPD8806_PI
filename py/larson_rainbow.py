# !/usr/bin/python

from bootstrap import *
from raspledstrip.animation import *
n = 30 # Number of times to move left to right

anim = LarsonRainbow(led, 2, 0.5)
for i in range(led.last_index * n):
    anim.step()
    led.update()
#sleep(0.03)

led.all_off()

