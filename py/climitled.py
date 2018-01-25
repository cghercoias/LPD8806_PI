#!/usr/bin/python


from bootstrap import *
from raspledstrip.animation import *

n = 48
while (1>0):
        for x in range (0,n): #odds
		if (x%2 ==1):
			led.fill(Color(255,0,175),x,x)
		if (x%2 ==0):
			led.fill(Color(0,0,0),x,x)
	led.update()
	time.sleep(.5)
	for x in range (0,n): #evens
                if (x%2 ==0):
                        led.fill(Color(255,0,175),x,x)
                if (x%2 ==1):
                        led.fill(Color(0,0,0),x,x)
        led.update()
	time.sleep(.5)

                
