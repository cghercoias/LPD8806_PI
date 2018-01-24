
# !/usr/bin/python

from bootstrap import *
from raspledstrip.animation import *
from time import sleep

#setup colors for wipe and chase
colors = [
    Color(255, 0, 0),
    Color(0, 255, 0),
    Color(0, 0, 255),
    Color(255, 255, 255),
]
while (True):
	for c in range(1):
    		anim = ColorWipe(led, colors[c])
		time.sleep(.5)
    	for i in range(led_count+1):
        	anim.step()
        	led.update()
    	time.sleep(0.5)

