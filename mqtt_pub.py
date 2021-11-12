import paho.mqtt.client as mqtt

# CREATE A CLIENT OBJECT
client=mqtt.Client()

while 1:
 # CONNECT WITH BROKER
 try:
  client.connect('broker.hivemq.com',1883)
  print ('Broker is Connected')
 except:
  print ('Broker Connection Failure')
 k=str(raw_input('Enter Message: '))
 client.publish('madblocks',k)
