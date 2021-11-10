import ORL_DHT
import time

sensor = ORL_DHT.DHT11

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23
pin = 16

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = ORL_DHT.read_retry(sensor, pin)

def read():
	if humidity is not None and temperature is not None:
    		tem=temperature
		hum=humidity
		#print("TEMP:"+str(tem))
		#print("HUM:"+str(hum))
		time.sleep(2)
		return(tem,hum)	
	else:
    		print('Failed to get reading. Try again!')
