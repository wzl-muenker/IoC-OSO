# File to test end execute the discreteTimeEngine

from src.utilities.precedence_analyzer import *
from src.utilities.py_object_json_serializer import *
from src.utilities.graph_visualization import *

import time
import jsonpickle
import json

def main():
    # Import data content
    from examples.scenario_informationsmodell_VÖ import projectList
    precedence_path = '../../ioc_construction_simulation/data/IoC_AG_IL_Informationsmodell_PrecedenceGraph.csv'
    building_element_path = '../../ioc_construction_simulation/data/IoC_AG_IL_Informationsmodell_BuildingElementInfo.csv'
    precedence_df = importPrecedenceGraph(precedence_path, building_element_path)

    test_building_element_list = deserialize_all_building_elements('IoC_bus_stop_scenario/building_elements/')
    test_project = Project('PR_0001', 'IoC_Project', test_building_element_list, projectList[0].resource_list)

    # Adding precedence information to building_element_list
    predecessor_handler = PredecessorHandler(projectList[0].BuildingElementList, precedence_df)
    predecessor_handler.add_predecessors_to_all_building_elements()
    building_element_list = predecessor_handler.building_element_list

    # Setup MQTT communication
    print("\nMQTT client initialized.")
    print("building element models read.")
    print("resource models read.")
    app_client = MQTT_client('bus_stop_project')
    for building_element in projectList[0].BuildingElementList:
        json_data = json.loads(jsonpickle.encode(building_element))
        app_client.publish('building_elements/' + building_element.id, json_data)
    time.sleep(1)
    for resource in projectList[0].resource_list:
        json_data = json.loads(jsonpickle.encode(resource))
        app_client.publish('resources/' + resource.id, json_data)


    # Setup simulation model
    model = DiscreteTimeModel()
    model.set_precedence_info(precedence_df)
    model.set_resource_info(projectList[0].resource_list)
    model.set_project_info(projectList)

    # Networkx Graph Layout


    print("\n--- Analyze current action ---.\n")
    print("building_element: ", model.building_element_list[1].id)
    print("reference_process: ", model.building_element_list[1].reference_process.id)
    print("current_activity: ", model.building_element_list[1].reference_process.activities[0].id)
    model.building_element_list[1].reference_process.activities[1].set_completed()
    model.building_element_list[1].reference_process.activities[2].set_completed()
    model.building_element_list[1].reference_process.activities[3].set_completed()

    print("\n get possible resources...")
    get_feasibility_tree_graph(model, building_element_index=2)

if __name__ == '__main__':
    main()










