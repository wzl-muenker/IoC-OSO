import paho.mqtt.client as mqtt
import time
import sys
import uuid
import json
import datetime
import numpy
import struct


MQTT_USERNAME = "xx"
MQTT_PASSWORD = "xxx"
MQTT_BROKER_ADDRESS = "test.mosquitto.org"
MQTT_BROKER_PORT = 1883

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_publish(client, userdata, mid):
    pass
    #print("[{}]".format(time.perf_counter()))

client = mqtt.Client()
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish


if __name__=="__main__":
    client.connect(MQTT_BROKER_ADDRESS, MQTT_BROKER_PORT, 60)
    client.loop_start()
    while True:
        try:
            client.publish("IoC-3c7cc2c2-53af-4180-a050-2630fdd80d8b/building_elements/be_001",json.dumps({"Hello" : "Test"}),0)
            print('Just published ', json.dumps({"Hello" : "Test"}))
            time.sleep(1)
        except KeyboardInterrupt:
            break
        
    client.loop_stop()
