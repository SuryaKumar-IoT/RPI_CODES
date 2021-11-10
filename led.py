import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 

led = 21

GPIO.setup(led,GPIO.OUT)

def ledon():
	GPIO.output(led,GPIO.LOW)
	time.sleep(0.5)
	print 'led On'
	
def ledoff():
	GPIO.output(led,GPIO.HIGH)
	time.sleep(0.5)
	print 'led Off'

def ledblink():
	ledon()
	ledoff()
	
