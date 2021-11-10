import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

relay = 21

GPIO.setup(relay,GPIO.OUT)
GPIO.output(relay,GPIO.LOW)
def relayon():
	print 'relay on'
        GPIO.output(relay,GPIO.HIGH)
        time.sleep(1)

def relayoff():
	print 'relay off'
        GPIO.output(relay,GPIO.LOW)
        time.sleep(1)

def relayblink():
        relayon()
        relayoff()

while True:
	relayblink()

