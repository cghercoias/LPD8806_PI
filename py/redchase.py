#!/usr/bin/python

from bootstrap import *
from raspledstrip.animation import *
numLED = 3 #ONLY CHANGE THIS NUMBER!!!!!!!
startnum = 1
number = 2
led.fill(Color(255,0,0),0,numLED-1)
led.fill(Color(0,0,0),0,0)
led.update()
time.sleep(.5)
led.fill(Color(255,0,0),1,3)
led.fill(Color(0,0,0),0,0)
led.update()
time.sleep(.5)
while (1>0):
	#led.fill(Color(255,0,0),0,0)
	#led.update()
	#time.sleep(1)
	#led.fill(Color(255,0,0),0,0)
	#led.update()
	#time.sleep(1)
	#while(startnum < 45):
		#startnum = startnum
        	#for x in range (0,numLED):
                	#led.fill(Color(255,0,0),startnum+x,startnum+x)
        	#led.fill(Color(0,0,0),startnum-1,startnum-1)
        	#led.update()
		#startnum = startnum
		#time.sleep(.5)
	#startnum = 1
	#led.all_off()


        led.fill(Color(255,0,0),startnum-1,startnum+1)
        led.fill(Color(0,0,0),startnum-2,startnum-2)
        led.update()
	time.sleep(.5)
	startnum = startnum + 1
