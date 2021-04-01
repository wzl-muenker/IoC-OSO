from src.IoC_OSO.class_models import *
from src.utilities.import_helper import *
from src.application.feasibility_checker import *
import random
import pandas as pd

class DiscreteTimeModel():
    def set_precedence_info(self, precedence_df):
        pass

    def set_project_info(self, project_list):
        self.project = project_list
        self.building_element_list = self.project[0].BuildingElementList

    def set_resource_info(self, resource_list):
        self.resource_list = resource_list

    def solve_greedy(self, greedy_strategy):
        time = 0

        # TODO: Implement positions

        # TODO: Make condition more understandable. While not every building_element is completed?
        while self.project[0].uncompleted_elements_remain():

            # Ist eine Resource wieder frei?
            self.resource_list = update_resources_availability(self.resource_list, time)
            print(self.resource_list)

            # Assembly Process Block
            for building_element in self.building_element_list:
                if building_element.in_Right_Position == 0:
                    solve_greedy_transport(self, time, building_element, greedy_strategy)
                else:
                    solve_greedy_assembly(self, time, building_element, greedy_strategy)
            time += 1
        time_table = create_table(self.building_element_list, self.resource_list, time)
        return time_table

def solve_greedy_transport(self, time, building_element, greedy_strategy):
    # TODO location and transport needs to be added
    # TODO allocateRessource parameter can be replaced

    transport_activities = building_element.reference_process.get_all_tranport_activities()
    # wurde ein Transport abgeschlossen
    if transport_activities[-1].get_end_time() <= time and \
            transport_activities[-1].state == State.TRANSPORT:
        building_element.in_Right_Position = 1
        building_element.state = State.INPOSITION
        solve_greedy_assembly(self, time, building_element, greedy_strategy)

    # kann ein neues Element gestartet werden?
    if building_element.possible_start_transport():
        building_element.start(time)
        building_element.reference_process.start(time)
        allocate_resources(transport_activities[0], self.resource_list, time, greedy_strategy,
                           assembly_or_transport="TRANSPORT")
        if transport_activities[0].allocatedResources:
            pass
        else:
            building_element.state = State.WAITING

    # können Elemente gestartet werden, die warten?
    if transport_activities[0].waitTime <= time and \
            transport_activities[0].state == State.WAITING:
        allocate_resources(transport_activities[0], self.resource_list, time, greedy_strategy,
                            assembly_or_transport="TRANSPORT")
        if transport_activities[0].allocatedResources:
            building_element.state = State.INPROGRESS
        else:
            building_element.state = State.WAITING


def solve_greedy_assembly(self, time, building_element, greedy_strategy):
    assembly_activities = building_element.reference_process.get_all_assembly_activities()
    # wurde eine Aktivität abgeschlossen
    for activity in assembly_activities:
        if activity.endTime <= time and activity.state == State.INPROGRESS:
            activity.set_completed()
            if assembly_activities[-1].state == State.COMPLETED:
                building_element.reference_process.set_completed()
                building_element.set_completed()
            else:
                next_activity = building_element.reference_process.get_next_activity(activity)
                allocate_resources(next_activity, self.resource_list, time, greedy_strategy,
                                   assembly_or_transport="ASSEMBLY")

    # kann ein neues Element gestartet werden?
    if building_element.state != State.COMPLETED:
        if building_element.possible_start_assembly():
            building_element.state = State.INPROGRESS
            allocate_resources(assembly_activities[0], self.resource_list,
                               time,
                               greedy_strategy, assembly_or_transport="ASSEMBLY")

    # können activitys gestartet werden, die warten?
    for waitingActivity in assembly_activities:
        if waitingActivity.waitTime <= time and waitingActivity.state == State.WAITING:
            allocate_resources(waitingActivity, self.resource_list, time, greedy_strategy,
                               assembly_or_transport="ASSEMBLY")

def allocate_resources(activity, resource_list, time, greedy_parameter, assembly_or_transport):
    for needed_capability in activity.capabilities:
        needed_capability.possible_resources = get_possible_resources_by_capability(resource_list, needed_capability)
    select_resources_and_calculate_time(activity, time, greedy_parameter, assembly_or_transport)

def select_resources_and_calculate_time(activity, time, greedyParameter, assembly_or_transport):
    # algorithm to choose the right resource, needs to be coded, atm gives the first resource back, if it is IDLE, otherwise waits for the first Resource to be idle
    # needs to check if resource is IDLE, if all resources are busy, we need to wait for the next available resource
    # changes state of resource in busy
    feasability_checks = []
    fitPossibile = []
    changePossibile = []
    for capability in activity.capabilities:
        capability.fittingResourcen = []
        capability.changeSetupResourcen = []
        capability.bussyResourcen = []
    for capability in activity.capabilities:
        for setting in capability.possible_resources:
            #TODO: resolve setting in resource and address directly
            # setting[0] -> resource
            # setting[1] -> tool
            # setting[2] -> capability
            # setting[3] -> parameters
            if setting[0].state == State.IDLE:
                if setting[0].get_current_setup() == setting[1].id:
                    capability.fittingResourcen.append(setting)
                    capability.bussyResourcen.append(setting)
                else:
                    capability.changeSetupResourcen.append(setting)
                    capability.bussyResourcen.append(setting)
            else:
                capability.bussyResourcen.append(setting)
        if capability.fittingResourcen:
            feasability_checks.append(True)
        else:
            fitPossibile.append(False)
        if capability.changeSetupResourcen:
            changePossibile.append(True)
        else:
            changePossibile.append(False)
    if all_conditions_feasible(fitPossibile):
        start_activity(activity, greedyParameter, time, assembly_or_transport)
    elif all_conditions_feasible(changePossibile):
        start_activity(activity, greedyParameter, time, assembly_or_transport)
    else:
        activity.set_wait_time()

#checks if all items in the list are true, returns true
def all_conditions_feasible(list):
    for item in list:
        if item == False:
            return False
    return True

def update_resources_availability(resource_list, time):
    for resource in resource_list:
        if resource.get_bussy_time() <= time:
            resource.release()
    return resource_list

def set_greedy_strategy(activity, greedyParameter):
    for capability in activity.capabilities:
        if greedyParameter == "FIRST":
            # nimmt die erste Resource,
            activity.set_used_resource(capability.fittingResourcen[0])
        elif greedyParameter == "FAST":
            # nimmt die schnellste Resource
            fastestResource = capability.get_best_resource(capability.fittingResourcen)
            activity.set_used_resource(fastestResource)
        elif greedyParameter == "RANDOM":
            # nimmt irgendeine Resource
            number = random.randint(0, len(capability.fittingResourcen) - 1)
            activity.set_used_resource(capability.fittingResourcen[number])

def create_table(buildingElementList, resourcen, time):
    time_table = []
    i = 0
    while i < time-1:
        time_table.append(i)
        i += 1
    time_table_df = pd.DataFrame(columns=(time_table), index=[resourcen])
    for building_element in buildingElementList:
        for activity in building_element.reference_process.activities:
            for usedResources in activity.allocatedResources:
                t = activity.startTime
                while t < activity.endTime:
                    time_table_df.at[usedResources[0], t] = activity.id
                    t +=1
    return time_table_df

def start_activity(activity, greedyParameter, time, assembly_or_transport):
    set_greedy_strategy(activity, greedyParameter)
    if assembly_or_transport == "ASSEMBLY":
        activity.start_activity_assembly(time)
        activity.set_duration()
        activity.set_end_time()
        for usedResource in activity.allocatedResources:
            usedResource[0].seize(activity)
    elif assembly_or_transport == "TRANSPORT":
        all_activities = activity.building_element.reference_process.get_all_tranport_activities()
        used_resources = activity.allocatedResources
        activity.allocatedResources = []
        for one_activity in all_activities:
            one_activity.start_activity_transport(time)
            one_activity.set_used_resource(used_resources[0])#only one resource is considerd
            one_activity.set_duration()
            one_activity.set_end_time()
            time = one_activity.endTime
        for used_resource in one_activity.allocatedResources:
            used_resource[0].seize(one_activity)

