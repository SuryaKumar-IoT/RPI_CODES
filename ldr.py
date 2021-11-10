import RPi.GPIO as GPIO
import led

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ldr=16

GPIO.setup(ldr,GPIO.IN)

while True:
        if(GPIO.input(ldr)==0):
                print("LDR SENSOR DETECTED")
                led.ledoff()
        else:
                print("SENSOR NOT DETECTED")
                led.ledon()


