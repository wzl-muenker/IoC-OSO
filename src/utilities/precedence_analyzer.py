# Auxiliary functions to write precedence functions in building elements

import numpy as np

class PredecessorHandler():
    def __init__(self, building_element_list, precedence_df):
        self.building_element_list = building_element_list
        self.precedence_df = precedence_df

    def get_direct_building_element_predecessors(self, building_element):
        building_element_index = self.precedence_df[self.precedence_df['name'] == building_element.name].index.to_list()
        predecessor_indices = np.where(self.precedence_df[building_element_index] == 1)[0]
        predecessor_names = self.precedence_df.iloc[predecessor_indices]['name'].values
        return(predecessor_names)

    def add_predecessors_to_all_building_elements(self):
        used_predecessor = []
        for buildingElement in self.building_element_list:
            predecessors = self.get_direct_building_element_predecessors(buildingElement)
            for predecessor_element in predecessors:
                for building_element in self.building_element_list:
                    if building_element.name == predecessor_element:
                        used_predecessor.append(building_element)
            buildingElement.predecessors = used_predecessor
            used_predecessor = []