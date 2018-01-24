from bootstrap import *
from raspledstrip.animation import *

for x in range(5):
	led.fill(Color(255,255,255),0,92)
	led.update()
	time.sleep(.07)
	led.all_off()
	time.sleep(.07)
