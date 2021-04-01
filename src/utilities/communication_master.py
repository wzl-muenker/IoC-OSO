from src.IoC_OSO.class_models import *

import paho.mqtt.client as mqtt
import json

class MQTT_client():
    def __init__(self, project_topic):
        self.MQTT_USERNAME = "xx"
        self.MQTT_PASSWORD = "xxx"
        self.MQTT_BROKER_ADDRESS = "test.mosquitto.org"
        self.MQTT_BROKER_PORT = 1883
        self.ROOT_TOPIC = 'IoC-3c7cc2c2-53af-4180-a050-2630fdd80d8b'
        self.PROJECT_TOPIC = project_topic
        self.start_client()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))

    def on_message(self, client, userdata, msg):
        try:
            # content = json.loads(msg.payload.decode("utf-8"))
            print(msg.topic, msg.payload.decode(
                "utf-8"))  # outfile.write("{}\t{}\t{}\t{}".format(*content["timestamp"], *content["value"])+ "\r\n")
            # outfile.flush()
        except Exception as exc:
            print("[ERROR] {}".format(exc))

    def start_client(self):
        self.client = mqtt.Client()
        self.client.username_pw_set(self.MQTT_USERNAME, self.MQTT_PASSWORD)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        #self.client.on_publish = self.on_publish
        #connect
        self.client.connect(self.MQTT_BROKER_ADDRESS, self.MQTT_BROKER_PORT, 60)
        #self.client.loop_start()

    def publish(self, topic, json_message):
        to_topic = str(self.ROOT_TOPIC + '/' + self.PROJECT_TOPIC + '/' + topic)
        self.client.publish(to_topic, json.dumps(json_message), 0)


    '''
    def on_publish(client, userdata, mid):
        pass
        # print("[{}]".format(time.perf_counter()))
    '''



