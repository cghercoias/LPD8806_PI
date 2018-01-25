#!/usr/bin/python


from bootstrap import *
from raspledstrip.animation import *
numstrips = 10
n = 16*numstrips
numLED = 8
startnum = 0
endnum = startnum+numLED
led.fill(Color(0,0,255),0,1)
led.update()
while (1>0):
	#for x in range(numLED):
		#led.fill(Color(0,0,255),0,x)
        led.fill(Color(0,255,0),0,1)
        led.update()
	#time.sleep(.3)
        led.fill(Color(0,255,0),0,2)
        led.update()
	#time.sleep(.3)
        led.fill(Color(0,255,0),0,3)
        led.update()
	#time.sleep(.3)
        led.fill(Color(0,255,0),0,4)
        led.update()
	#time.sleep(.3)
        led.fill(Color(0,255,0),0,5)
        led.update()
	#time.sleep(.3)
        led.fill(Color(0,255,0),0,6)
        led.update()
	#time.sleep(.3)
	led.fill(Color(0,255,0),0,7)
	led.update()
	#time.sleep(.3)

        while (endnum < n-1): #going there
		print "start"
                endnum = startnum+numLED
                led.fill(Color(0,255,0),startnum,endnum)
                led.fill(Color(0,0,0),0,startnum-1)
                led.update()
		#time.sleep(.3)
                startnum = startnum +1
                print startnum


	led.fill(Color(0,0,0),n-(numLED-1),n-(numLED))
	led.fill(Color(0,255,0),n-(numLED-2),n-1)
	led.fill(Color(0,0,0),40,40)
	led.update()
	#time.sleep(.3)
	led.fill(Color(0,255,0),n-(numLED-3),n)
	led.fill(Color(0,0,0),n-(numLED-2),n)
	led.update()
	#time.sleep(.3)
	led.fill(Color(0,255,0),n-(numLED-4),n)
	led.fill(Color(0,0,0),n-(numLED-3),n-(numLED-3))
	led.update()
	#time.sleep(.3)
	led.fill(Color(0,255,0),n-(numLED-5),n)
	led.fill(Color(0,0,0),n-(numLED-4),n-(numLED-4))
	led.update()
	#time.sleep(.3)
	led.fill(Color(0,255,0),n-(numLED-6),n)
	led.fill(Color(0,0,0),n-(numLED-5),n-(numLED-5))
	led.update()
	#time.sleep(.3)
	led.fill(Color(0,255,0),46,48)
	led.fill(Color(0,0,0),45,45)
	led.update()
	#time.sleep(.3)
	led.fill(Color(0,255,0),47,48)
	led.fill(Color(0,0,0),46,46)
	led.update()
	#time.sleep(.3)
	led.fill(Color(0,255,0),48,48)
	led.fill(Color(0,0,0),47,47)
	led.update()
	#time.sleep(.3)
	led.fill(Color(0,0,0),48,48)
	led.update()
	#time.sleep(.3)
	startnum = 0
	endnum = startnum+numLED
       # while (startnum > 0): #going back
                #endnum = startnum+numLED
                #led.fill(Color(0,255,0),startnum-1,endnum)
                #led.fill(Color(0,0,0),endnum+1,n)
                #led.update()
                #startnum = startnum-1
                #print startnum



