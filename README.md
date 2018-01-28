Overview 
====
A Python library for the Raspberry Pi to drive LPD8806 based RGB light strips.

Initial code from: https://github.com/Sh4d/LPD8806

Getting Started 
---------------
First off, you need to enable SPI if it hasn't been already. 
The easiest way to do this in Raspbian is via raspi-config. 
At the command line, type:

```
sudo raspi-config
```

It will load a menu with a blue background. 
Arrow down to option 8, "Advanced Options" and hit Enter. 
Then select option A5 "SPI" and hit Enter again. 
It will ask you if you want to enable SPI, select yes. 
Once back to the main menu, select <Finish> and you're done!

Next, wiring your LPD8806 strips.
Connect as follows:

```
RaspberryPi MOSI (pin 10) -> Strand DI (DataIn)
RaspberryPi SCLK (pin 12) -> Strand CI (ClockIn)
````

Most strips use around 10W per meter (for ~32 LEDs/m) or 2A at 5V.
The RaspberryPi cannot even come close to this so a larger power supply is required, 
however, due to voltage loss along long runs you will need to put in a new power supply at least every 5 meters.
Technically you can power the RaspberryPi through the GPIO pins and use the same supply as the strips, 
but I would NOT recommend it. Using the microUSB power connector it's a much safer option.

Also, while it *should* work without it, to be safe you should add a level converter 
between the RaspberryPi and the strip's data lines. This will also help you have longer runs.

cd to the LPD8806_PI directory where requirements.txt is located.
```
run: pip install -r requirements.txt in your shell.
```
In some cases, using py-spidev can have better performance but is compeltely optional. 
To install it, run the following commands:

```
sudo apt-get install python-dev
git clone https://github.com/doceme/py-spidev.git
cd py-spidev/
sudo python setup.py install
````

Then set the second parameter of LEDStrip to True to enable py-spidev.
In the folder LPD8806_PI, run "python setup.py install" to install the software.

```
git clone https://github.com/adammhaile/RPi-LPD8806.git
cd RPi-LPD8806
python setup.py install
python example.py
```

You should see your LED strip run through a number of animations. 
Here is a basic program that will fill the entire strip Red:
```
~$ python
Python 2.7.13 (default, Nov 24 2017, 17:33:09)
[GCC 6.3.0 20170516] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>from raspledstrip.ledstrip import *
>>>led = LEDStrip(48)
>>>led.fillRGB(255,0,0)
>>>led.update()
``` 
LEDStrip() initializes the class to control the strip and takes the number of LEDs as the argument. 
The arguments for led.fillRGB() are Red (0-255), Blue (0-255) and Green (0-255). 
Finally led.update() writes the colors out to the strip. 
The LED strip won't change until led.update is called (common mistake). 

Animations
----------
The library contains a number of animations. Below is a list of animations available.
* Rainbow
* Color Wipe
* Color Chase
* Larson Scanner (Cylon Eye, K.I.T.T)
* Wave
* Color Pattern


More Info
---------

Download, extract, then run the help:
```
pi@raspberrypi~$ python
Python 2.7.13 (default, Nov 24 2017, 17:33:09)
[GCC 6.3.0 20170516] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import LPD8806
>>> help(LPD8806)
```
- The LPD8806 chip does not seem to really specify in what order the color channels are, so there is a helper function in case yours happen to be different. The most common seems to be GRB order but I have found some strips that use BRG order as well. If yours (like the one's from Adafruit) use GRB order nothing needs to be done as this is the default. But if the channels are swapped call the method setChannelOrder() with the proper ChannelOrder value. Those are the only two I've ever encountered, but if anyone ever encounters another, please let me know so I can add it.
 
- All of the animations are designed to allow you to do other things on the same thread in between frames. So, everytime you want to actually progress the animation, call it's method and then call update() to push the data to the the strip. You could do any other processing on the buffer before pushing the update if needed. Each animation has a step variable that can be manually reset or modified externally. See variables in the __init__ of LEDStrip
 
- If any of the built in animations are not enough you can use any of the set or fill methods to manually manipulate the strip data.
 
- These strips can get extremely bright (the above video was filmed using 50% brightness) so you can use setMasterBrightness() to set a global level which all output values are multiplied by. This way you don't have to manually modify all of the RGB values to adjust the levels. However, Color takes an optional brightness value so that it can be set on an individual level. Last, if using HSV, you can just set it's "Value" component to adjust the brightness level.
 
- ColorHSV is there for easily fading through a natural color progression. However, all methods take a Color object, so call ColorHSV.getColorRGB() before passing to any of the set, fill, or animation methods.
