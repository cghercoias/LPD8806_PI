from bootstrap import *
from raspledstrip.animation import *

colors = [
    (255.0, 0.0, 0.0),
    (0.0, 255.0, 0.0),
    (0.0, 0.0, 255.0),
    (255.0, 255.0, 255.0),
]

for c in range(4):
    anim = ColorChase(led, colors[c])

    for i in range(led_count):
        anim.step()
        led.update()
    #sleep(0.03)

led.fill_off()

