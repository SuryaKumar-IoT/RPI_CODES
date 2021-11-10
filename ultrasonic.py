import RPi.GPIO as GPIO
import time

def measure():
  stop=0
  # This function measures a distance
  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()
  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()
  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()
  elapsed = stop-start
  distance = (elapsed * 34300)/2
  print(distance)
  if(distance<=0):
   distance=0
  if(distance<30):
   print("object detected")
   stopp()
  else:
   print("Normal")
   front()

GPIO.setmode(GPIO.BCM)
# Define GPIO to use on Pi
GPIO_TRIGGER = 12
GPIO_ECHO    = 13
print "Ultrasonic Measurement"

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)
while True:
	measure()
        time.sleep(1)
