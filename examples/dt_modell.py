# File to test end execute the discreteTimeEngine

from src.utilities.precedence_analyzer import *
from src.application.discrete_time_engine import *
from src.utilities.py_object_json_serializer import *
from src.utilities.communication_master import *

import time
import networkx as nx
import matplotlib.pyplot as plt
import jsonpickle
import json


# Import data content
from examples.scenario_informationsmodell_VÖ import projectList
#precedence_path = '../../ioc_construction_simulation/data/IoC_AG_IL_Informationsmodell_PrecedenceGraph.csv'
#building_element_path = '../../ioc_construction_simulation/data/IoC_AG_IL_Informationsmodell_BuildingElementInfo.csv'
#precedence_df = importPrecedenceGraph(precedence_path, building_element_path)

#test_building_element_list = deserialize_all_building_elements('IoC_bus_stop_scenario/building_elements/')
#test_project = Project('PR_0001', 'IoC_Project', test_building_element_list, projectList[0].resource_list)

# Adding precedence information to building_element_list
#predecessor_handler = PredecessorHandler(projectList[0].BuildingElementList, precedence_df)
#predecessor_handler.add_predecessors_to_all_building_elements()
#building_element_list = predecessor_handler.building_element_list

# Setup MQTT communication


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

