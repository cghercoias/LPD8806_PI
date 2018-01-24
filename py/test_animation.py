from raspledstrip.ledstrip import LEDStrip
from raspledstrip.LPD8806 import LPD8806SPI
from raspledstrip.animation import AlertStrobe, FillFromCenter, BreathingLight
from raspledstrip.color import Color

led_strip = LEDStrip(LPD8806SPI(36))
led_strip.all_off()

alert_color = Color(255, 0, 0, 1.0)
fill_animation = FillFromCenter(led_strip, alert_color)
fill_animation.run(1, 30, 18)
alert_animation = AlertStrobe(led_strip, alert_color)
alert_animation.run(1, 20, 24)
led_strip.all_off()
fill_animation = BreathingLight(led_strip, 0, 255, 0, 0.1, 1.0, 0, 0)
fill_animation.run(1, 30, 1000)
led_strip.all_off()

