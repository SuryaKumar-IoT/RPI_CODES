import dhttest as dht
import urllib2

while True:
	t=dht.read()
	#print(t)
	temp=t[0]
	hum=t[1]
	print("Temperature:"+ str(temp))
	print("Humidity:"+str(hum))
	res=urllib2.urlopen('https://api.thingspeak.com/update?api_key=F7O3ITDYJO0DYK11&field1='+str(temp)+'&field2='+str(hum))
	print(res)
