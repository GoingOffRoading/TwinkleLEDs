# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *
from random import randint

# LED strip configuration:
LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


# Define functions which animate LEDs in various ways.

def setPixelColorRGB(strip, n, red, green, blue, white = 0):
	"""Set LED at position n to the provided red, green, and blue color.
	Each color component should be a value from 0 to 255 (where 0 is the
	lowest intensity and 255 is the highest intensity).
	"""
	strip.setPixelColor(n, Color(red, green, blue, white))
	
# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
		setPixelColorRGB (randint(1,22), randint(0,150), randint(0,150), randint(0,150), 0) 
		time.sleep(1)
