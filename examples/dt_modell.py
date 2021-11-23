# File to test end execute the discreteTimeEngine

from src.utilities.communication_master import *

import time
import jsonpickle
import json

from examples.scenario_informationsmodell_VÖ import projectList


if __name__=="__main__":
    dt_client = MQTT_client('bus_stop_project')
    print("DT clients initialized.")

    # publish initial building elements
    print("\n --- building element data ---\n")
    for building_element in projectList[0].BuildingElementList:
        json_data = json.loads(jsonpickle.encode(building_element))
        print("JSON data loaded: ", building_element.id)
        dt_client.publish('building_elements/' + building_element.id, json_data)
        print("Static use case data published: ", building_element.id)
    time.sleep(1)

    # publish initial resource elements
    print("\n --- resource data ---\n")
    for resource in projectList[0].resource_list:
        print("JSON data loaded: ", resource.id)
        json_data = json.loads(jsonpickle.encode(resource))
        print("Static use case data published: ", resource.id)
        dt_client.publish('resources/' + resource.id, json_data)

    # subscribe to changes
    print("\n --- Subscribe to updates ---\n")
    dt_client.client.subscribe(dt_client.ROOT_TOPIC + '/#')
    
    dt_client.client.loop_forever()

