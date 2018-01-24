import math
import random

from color import *
import util


class BaseAnimation(object):
    def __init__(self, led_strip, start, end):
        self._led = led_strip
        self._start = start
        self._end = end
        if self._end == 0 or self._end > self._led.last_index:
            self._end = self._led.last_index

        self._size = self._end - self._start + 1
        self._step = 0

        self._time_ref = 0

    def __ms_time(self):
        return time.time() * 1000.0

    def step(self, amt=1):
        raise RuntimeError("Base class step() called. This shouldn't happen")

    def run(self, amt=1, sleep=None, max_steps=0):
        cur_step = self._step
        while max_steps == 0 or cur_step < max_steps:
            self._time_ref = self.__ms_time()
            self.step(amt)
            self._led.update()
            if sleep:
                diff = (self.__ms_time() - self._time_ref)
                t = max(0, (sleep - diff) / 1000.0)
                if t == 0:
                    print "Timeout of %dms is less than the minimum of %d!" % (sleep, diff)
                time.sleep(t)
            cur_step += 1


class Nothing(BaseAnimation):
    """Placeholder for killing time in animation scripts while keeping the LEDs off"""

    def __init__(self, led_strip, start=0, end=0):
        super(Nothing, self).__init__(led_strip, start, end)

    def step(self, amt=1):
        self._led.fill_off(self._start, self._end)
        self._step += amt


class Rainbow(BaseAnimation):
    """Generate rainbow."""

    def __init__(self, led_strip, start=0, end=0):
        super(Rainbow, self).__init__(led_strip, start, end)

    def step(self, amt=1):

        for i in range(self._size):
            color = (i + self._step) % 384
            self._led.set(self._start + i, wheel_color(color))

        self._step += amt
        overflow = self._step - 384
        if overflow >= 0:
            self._step = overflow


class RainbowCycle(BaseAnimation):
    """Generate rainbow wheel equally distributed over strip."""

    def __init__(self, led_strip, start=0, end=0):
        super(RainbowCycle, self).__init__(led_strip, start, end)

    def step(self, amt=1):
        for i in range(self._size):
            color = (i * (384 / self._size) + self._step) % 384
            self._led.set(self._start + i, wheel_color(color))

        self._step += amt
        overflow = self._step - 384
        if overflow >= 0:
            self._step = overflow


class ColorPattern(BaseAnimation):
    """Fill the dots progressively along the strip with alternating colors."""

    def __init__(self, led_strip, colors, width, dir=True, start=0, end=0):
        super(ColorPattern, self).__init__(led_strip, start, end)
        self._colors = colors
        self._colorCount = len(colors)
        self._width = width
        self._total_width = self._width * self._colorCount
        self._dir = dir

    def step(self, amt=1):
        for i in range(self._size):
            cIndex = ((i + self._step) % self._total_width) / self._width
            self._led.set(self._start + i, self._colors[cIndex])
        if self._dir:
            self._step += amt
            overflow = (self._start + self._step) - self._end
            if overflow >= 0:
                self._step = overflow
        else:
            self._step -= amt
            if self._step < 0:
                self._step = self._end + self._step


class ColorWipe(BaseAnimation):
    """Fill the dots progressively along the strip."""

    def __init__(self, led_strip, color, start=0, end=0):
        super(ColorWipe, self).__init__(led_strip, start, end)
        self._color = color

    def step(self, amt=1):
        if self._step == 0:
            self._led.fill_off()
        for i in range(amt):
            self._led.set(self._start + self._step - i, self._color)

        self._step += amt
        overflow = (self._start + self._step) - self._end
        if overflow >= 0:
            self._step = overflow


class ColorFade(BaseAnimation):
    """Fill the dots progressively along the strip."""

    def __init__(self, led_strip, colors, step=0.1, start=0, end=0):
        super(ColorFade, self).__init__(led_strip, start, end)
        self._colors = colors
        self._levels = util.wave_range(0.4, 1.0, step)
        self._level_count = len(self._levels)
        self._color_count = len(colors)

    def step(self, amt=1):
        if self._step > self._level_count * self._color_count:
            self._step = 0

        c_index = (self._step / self._level_count) % self._color_count
        l_index = (self._step % self._level_count)
        color = self._colors[c_index]
        self._led.fill(Color(color.r, color.g, color.b, self._levels[l_index]), self._start, self._end)

        self._step += amt


class ColorChase(BaseAnimation):
    """Chase one pixel down the strip."""

    def __init__(self, led_strip, color, width=1, start=0, end=0):
        super(ColorChase, self).__init__(led_strip, start, end)
        self._color = color
        self._width = width

    def step(self, amt=1):
        if self._step == 0:
            self._led.set_off(self._end)
        else:
            self._led.fill_off()  # because I am lazy

        for i in range(self._width):
            self._led.set(self._start + self._step + i, self._color)

        self._step += amt
        overflow = (self._start + self._step) - self._end
        if overflow >= 0:
            self._step = overflow


class PartyMode(BaseAnimation):
    """Stobe Light Effect."""

    def __init__(self, led_strip, colors, start=0, end=0):
        super(PartyMode, self).__init__(led_strip, start, end)
        self._colors = colors
        self._color_count = len(colors)

    def step(self, amt=1):
        amt = 1  # anything other than 1 would be just plain silly
        if self._step > (self._color_count * 2) - 1:
            self._step = 0

        if self._step % 2 == 0:
            self._led.fill(self._colors[self._step / 2], self._start, self._end)
        else:
            self._led.fill_off()

        self._step += amt


class FireFlies(BaseAnimation):
    """Stobe Light Effect."""

    def __init__(self, led_strip, colors, width=1, count=1, start=0, end=0):
        super(FireFlies, self).__init__(led_strip, start, end)
        self._colors = colors
        self._color_count = len(colors)
        self._width = width
        self._count = count

    def step(self, amt=1):
        amt = 1  # anything other than 1 would be just plain silly
        if self._step > self._led.leds:
            self._step = 0

        self._led.fill_off()

        for i in range(self._count):
            pixel = random.randint(0, self._led.leds - 1)
            color = self._colors[random.randint(0, self._color_count - 1)]

            for i in range(self._width):
                if pixel + i < self._led.leds:
                    self._led.set(pixel + i, color)

        self._step += amt


class LarsonScanner(BaseAnimation):
    """Larson scanner (i.e. Cylon Eye or K.I.T.T.)."""

    def __init__(self, led_strip, color, tail=2, fade=0.75, start=0, end=0):
        super(LarsonScanner, self).__init__(led_strip, start, end)
        self._color = color

        self._tail = tail + 1  # makes tail math later easier
        if self._tail >= self._size / 2:
            self._tail = (self._size / 2) - 1

        self._fade = fade
        self._direction = -1
        self._last = 0

    def step(self, amt=1):
        self._last = self._start + self._step
        self._led.set(self._last, self._color)

        tl = self._tail
        if self._last + tl > self._end:
            tl = self._end - self._last
        tr = self._tail
        if self._last - tr < self._start:
            tr = self._last - self._start

        # clear the whole thing
        self._led.fill_off(self._start, self._end)

        for l in range(1, tl + 1):
            level = (float(self._tail - l) / float(self._tail)) * self._fade
            self._led.set_rgb(self._last + l,
                              self._color.r * level,
                              self._color.g * level,
                              self._color.b * level)

        if self._last + tl + 1 <= self._end:
            self._led.set_off(self._last + tl + 1)

        for r in range(1, tr + 1):
            level = (float(self._tail - r) / float(self._tail)) * self._fade
            self._led.set_rgb(self._last - r,
                              self._color.r * level,
                              self._color.g * level,
                              self._color.b * level)

        if self._last - tr - 1 >= self._start:
            self._led.set_off(self._last - tr - 1)

        if self._start + self._step >= self._end:
            self._direction = -self._direction
        elif self._step <= 0:
            self._direction = -self._direction

        self._step += self._direction * amt


class LarsonRainbow(LarsonScanner):
    """Larson scanner (i.e. Cylon Eye or K.I.T.T.) but Rainbow."""

    def __init__(self, led_strip, tail=2, fade=0.75, start=0, end=0):
        super(LarsonRainbow, self).__init__(
            led_strip, ColorHSV(0).get_color_rgb(), tail, fade, start, end)

    def step(self, amt=1):
        self._color = ColorHSV(self._step * (360 / self._size)).get_color_rgb()

        super(LarsonRainbow, self).step(amt)


class Wave(BaseAnimation):
    """Sine wave animation."""

    def __init__(self, led_strip, color, cycles, start=0, end=0):
        super(Wave, self).__init__(led_strip, start, end)
        self._color = color
        self._cycles = cycles

    def step(self, amt=1):
        for i in range(self._size):
            y = math.sin(
                math.pi *
                float(self._cycles) *
                float(self._step * i) /
                float(self._size))

            if y >= 0.0:
                # Peaks of sine wave are white
                y = 1.0 - y  # Translate Y to 0.0 (top) to 1.0 (center)
                c2 = Color(255 - float(255 - self._color.r) * y,
                           255 - float(255 - self._color.g) * y,
                           255 - float(255 - self._color.b) * y)
            else:
                # Troughs of sine wave are black
                y += 1.0  # Translate Y to 0.0 (bottom) to 1.0 (center)
                c2 = Color(float(self._color.r) * y,
                           float(self._color.g) * y,
                           float(self._color.b) * y)
            self._led.set(self._start + i, c2)

        self._step += amt


import time
import timecolors


class RGBClock(BaseAnimation):
    """RGB Clock done with RGB LED strip(s)"""

    def __init__(self, led_strip, h_start, h_end, m_start, m_end, s_start, s_end):
        super(RGBClock, self).__init__(led_strip, 0, 0)
        if h_end < h_start:
            h_end = h_start + 1
        if m_end < m_start:
            m_end = m_start + 1
        if s_end < s_start:
            s_end = s_start + 1
        self._hStart = h_start
        self._hEnd = h_end
        self._mStart = m_start
        self._mEnd = m_end
        self._sStart = s_start
        self._sEnd = s_end

    def step(self, amt=1):
        t = time.localtime()

        r, g, b = timecolors._hourColors[t.tm_hour]
        self._led.fill_rgb(r, g, b, self._hStart, self._hEnd)

        r, g, b = timecolors._minSecColors[t.tm_min]
        self._led.fill_rgb(r, g, b, self._mStart, self._mEnd)

        r, g, b = timecolors._minSecColors[t.tm_sec]
        self._led.fill_rgb(r, g, b, self._sStart, self._sEnd)

        self._step = 0


class AlertStrobe(BaseAnimation):
    def __init__(self, led_strip, strobe_color, start=0, end=0):
        self._color = strobe_color
        super(AlertStrobe, self).__init__(led_strip, start, end)

    def step(self, step_amount=1):
        self._led.fill(self._color) if self._step % 2 else self._led.all_off()
        self._step += step_amount


class FillFromCenter(BaseAnimation):
    def __init__(self, led_strip, fill_color, start=0, end=0):
        self._strip_length = led_strip.last_index
        self._center_point = int(self._strip_length / 2)
        self._color = fill_color
        super(FillFromCenter, self).__init__(led_strip, start, end)

    def step(self, step_amount=1):
        if self._step > self._center_point:
            self._step = 0
            self._led.fill_off()
        self._led.set(self._center_point + self._step, self._color)
        self._led.set(self._center_point - self._step, self._color)
        self._step += 1


class BreathingLight(BaseAnimation):
    def __init__(self, led_strip, red, green, blue, min_brightness, max_brightness, start=0, end=0):
        super(BreathingLight, self).__init__(led_strip, start, end)
        self._base_red = red
        self._base_green = green
        self._base_blue = blue
        self._min_bright = float(min_brightness)
        self._max_bright = float(max_brightness)
        self._direction = 1
        self._step = 1

    def scale_brightness(self, step_number):
        return self._min_bright + ((self._max_bright - self._min_bright) * (float(step_number) / 255))

    def step(self, step_amount=1):
        if self._step > 254 or self._step < 0:
            self._direction *= -1

        self._led.fill(
            Color(
                self._base_red,
                self._base_green,
                self._base_blue,
                self.scale_brightness(self._step)
            )
        )
        self._step += (1 * self._direction)

