from bootstrap import *
from raspledstrip.animation import *

c = 91 #Value of current
r = 127 
b = 0 
g = 0 
while (c > 90): #When (x) is greater than 10, flash lights
	anim = Wave(led, Color(r, b, g), 2)
	for i in range(led.last_index):
    		anim.step()
    		led.update()
while (c < 10):#When (x) is less than 10, turn off lights
	led.all_off()
			 




