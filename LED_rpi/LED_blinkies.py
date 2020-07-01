from gpiozero import LED
## from signal import pause
from time import sleep
import random

red = LED(15)
blue = LED(25)
green = LED(18)
yellow = LED(23)
white = LED(24)

waitArray = [0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001]

cycle1 = True

ledArray = [red, yellow, blue, green, white]

def blinker1(whatTimer, whatColor):

	blinkLength = random.randint(0,15)

	for x in range(blinkLength):
		whatColor.on()
		sleep(whatTimer)
		whatColor.off()
		sleep(whatTimer)


white (cycle1 == True):

	timeChoice = random.randint(0,9) * waitArray[random.randint(0,5)]
	n = random.randint(0,4)

	for y in range(5):
		blinker1(timeChoice, ledAddary[n])