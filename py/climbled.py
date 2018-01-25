#!/usr/bin/python


from bootstrap import *
from raspledstrip.animation import *

n = 48
startnum = 0
endnum = 1
while (1>0):
        while (endnum < n): #going there
                led.fill(Color(0,0,255),startnum,endnum)
		endnum = endnum + 1
                led.update()
        while (endnum > 1): #going back
                led.fill(Color(0,0,0),endnum,n-1)
		endnum = endnum - 1
                led.update()


