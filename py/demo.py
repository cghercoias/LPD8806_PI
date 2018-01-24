from bootstrap import *
from raspledstrip.animation import *


colors = [
    (255.0, 0.0, 0.0),
    (0.0, 255.0, 0.0),
    (0.0, 0.0, 255.0),
    (255.0, 255.0, 255.0),
]

anim = RainbowCycle(led)
for i in range(384 * 2):
    anim.step()
    led.update()

led.fill_off()


