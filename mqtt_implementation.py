# -*- coding: utf-8 -*-
"""MQTT Implementation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bFmYgQgVo6vz5RTVDI0uv_Y2TiYXJcwn

First We need Import Header FIle /Library which supports MQTT In python
"""

import paho.mqtt.client as mqtt

broker_url="broker.hivemq.com"
port=1883

def on_message(client,userdata,msg):
  print(msg.topic+":"+msg.payload.decode())

client=mqtt.Client()
client.on_message=on_message
client.connect(broker_url,port)
client.subscribe("iot/mb")
client.loop_forever()