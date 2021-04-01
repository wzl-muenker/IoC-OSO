from examples.scenario_informationsmodell_VÖ import *

import jsonpickle
import json
import os

# building elements
def serialize_all_building_elements():
    for building_element in projectList[0].BuildingElementList:
        print(building_element.id)

        building_element_json = jsonpickle.encode(building_element)

        directory = '../../examples/IoC_bus_stop_scenario/building_elements/'
        filename = directory + building_element.id + '.json'

        f = open(filename, "w")
        f.write(json.dumps(json.loads(building_element_json), indent=4, sort_keys=True))
        f.close()

def deserialize_all_building_elements(dir_path):
    building_element_list = []
    directory = os.fsencode(dir_path)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".json"):
            file_path = dir_path + filename
            with open(file_path) as json_file:
                data = json_file.read()
                building_element_list.append(jsonpickle.decode(data))

    return building_element_list

# resources
def serialize_all_resources():
    for resource in projectList[0].resource_list:
        print(resource.id)

        resource_json = jsonpickle.encode(resource)

        directory = '../../examples/IoC_bus_stop_scenario/resources/'
        filename = directory + resource.id + '.json'

        f = open(filename, "w")
        f.write(json.dumps(json.loads(resource_json), indent=4, sort_keys=True))
        f.close()

def deserialize_all_resources(dir_path):
    resource_list = []
    directory = os.fsencode(dir_path)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".json"):
            file_path = dir_path + filename
            with open(file_path) as json_file:
                data = json_file.read()
                resource_list.append(jsonpickle.decode(data))

    return resource_list

#building_element_list = deserialize_all_building_elements()
#print('done')