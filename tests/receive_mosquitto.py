import paho.mqtt.client as mqtt
import time
import sys
import datetime
import json

MQTT_USERNAME = "xx"
MQTT_PASSWORD = "xx"
MQTT_BROKER_ADDRESS = "test.mosquitto.org"
MQTT_BROKER_PORT = 1883

outfile = open(datetime.datetime.utcnow().isoformat().replace(":", "-") + "Z.txt", "w")

topic = "IoC-3c7cc2c2-53af-4180-a050-2630fdd80d8b/#"
if len(sys.argv) > 1:
    topic = sys.argv[1]

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    try:
        #content = json.loads(msg.payload.decode("utf-8"))
        print(msg.topic, msg.payload.decode("utf-8"))#outfile.write("{}\t{}\t{}\t{}".format(*content["timestamp"], *content["value"])+ "\r\n")
        #outfile.flush()
    except Exception as exc:
        print("[ERROR] {}".format(exc))
	
    #print("[{}] ".format(datetime.datetime.utcnow().isoformat() + "Z") + msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.on_connect = on_connect
client.on_message = on_message

if __name__=="__main__":
    client.connect(MQTT_BROKER_ADDRESS, MQTT_BROKER_PORT, 60)
    client.loop_forever()
    print("Use Ctrl+C to interrupt!")