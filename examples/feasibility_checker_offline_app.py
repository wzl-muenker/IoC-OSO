# File to test end execute the discreteTimeEngine without MQTT

from src.utilities.precedence_analyzer import *
from src.utilities.graph_visualization import *

def main():
    # Import data content
    from examples.scenario_informationsmodell_VÖ import projectList

    precedence_path = '../../ioc_construction_simulation/data/IoC_AG_IL_Informationsmodell_PrecedenceGraph.csv'
    building_element_path = '../../ioc_construction_simulation/data/IoC_AG_IL_Informationsmodell_BuildingElementInfo.csv'
    precedence_df = importPrecedenceGraph(precedence_path, building_element_path)

    # Adding precedence information to building_element_list
    predecessor_handler = PredecessorHandler(projectList[0].BuildingElementList, precedence_df)
    predecessor_handler.add_predecessors_to_all_building_elements()
    building_element_list = predecessor_handler.building_element_list


    # Setup simulation model
    model = DiscreteTimeModel()
    model.set_precedence_info(precedence_df)
    model.set_resource_info(projectList[0].resource_list)
    model.set_project_info(projectList)

    get_feasibility_tree_graph(model, building_element_index=1)

if __name__ == '__main__':
    main()
