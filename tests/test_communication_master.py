from src.utilities.communication_master import *

my_client = MQTT_client('test_topic/client1')
my_client.publish({"Hello" : "Test"})