import RPi.GPIO as GPIO
import led

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ir=16

GPIO.setup(ir,GPIO.IN)

while True:
	if(GPIO.input(ir)==1):
		print("IR SENSOR DETECTED")
		led.ledon()
	else:
		print("SENSOR NOT DETECTED")
		led.ledoff()

