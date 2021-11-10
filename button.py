import RPi.GPIO as GPIO
import led

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

sw=20

GPIO.setup(sw,GPIO.IN)

while True:
	if(GPIO.input(sw)==0):
		led.ledon()
	else:
		led.ledoff()

