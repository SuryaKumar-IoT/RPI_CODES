import RPi.GPIO as GPIO
import led

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

gas=16

GPIO.setup(gas,GPIO.IN)

while True:
        if(GPIO.input(gas)==0):
                print("GAS SENSOR DETECTED")
                led.ledon()
        else:
                print("SENSOR NOT DETECTED")
                led.ledoff()


