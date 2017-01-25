import time
import randomcolor

from random import randint
from neopixel import *

# LED strip configuration:
LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 50     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

# This generates an RGB color from the randomcolor plugin
rand_color = randomcolor.RandomColor()


# This is the animation for the LED
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
		# Color wipe animations.


		#Attempt 1: no idea of what I was thinking here
		#colorWipe(strip, Color(', '.join(map(str, rand_color.generate(format_='rgbArray')))))

 		
		#Attempt 2: I tried messing with the .replace function, no luck
		#rand_col = rand_color.generate(format_='rbgbArray').replace('[', '').replace(']', '')

		
		#Attempt 3: Your first idea
		#rand_col = rand_color.generate(format_='rbgbArray')
		#colorWipe(strip, Color(rand_col[0], rand_col[1], rand_cold[2]))
		#with this, I get a 'list index out of range' error		


		#Attempt 4: Your second idea
		rand_col = rand_color.generate(format_='rgbArray')
		colorWipe(strip, Color(*rand_col))
		#With this, I get a type error with a message like 'requires three arguments' whch makes me think that this is failing to strip something
