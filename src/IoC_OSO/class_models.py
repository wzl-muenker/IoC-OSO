
# -------CONSTANTS--------------
class State(object):
    IDLE = "IDLE"
    BUSY = "BUSY"
    COMPLETED = "COMPLETED"
    INPROGRESS = "IN PROGRESS"
    WAITING = "WAITING"
    TRANSPORT = "TRANSPORT"
    INPOSITION = "IN POSITION"


class Location(object):
    MACHINERY_STORAGE = [0, 0, 0]
    MATERIAL_STORAGE = [20, 20, 0]
    ASSEMBLY_STATION = [100, 100, 0]


class AssemblyActivityTypes(object):
    TRANSPORT = ["TRANSPORT", 10000]
    JUSTAGE = ["Justage", 10000]
    FIXIEREN = ["Fixieren", 10000]


class TransportActivityTypes(object):
    TRANSPORT = ["TRANSPORT", 10000]
    ABLADEN = ["ABLADEN", 10000]
    AUFNEHMEN = ["AUFNEHMEN", 10000]


class CapabilityTypes(object):
    TRANSPORT = "TRANSPORT"
    JUSTIEREN = "JUSTIEREN"
    FIXIEREN = "FIXIEREN"


class TransportCapabilityTypes(object):
    AUFNEHMEN = "AUFNEHMEN"
    TRANSPORT = "TRANSPORT"
    ABLADEN = "ABLADEN"


class ParameterTypes(object):
    FEASIBILITY_QUANTITATIVE = "FEASIBILITY_QUANTITATIVE"
    FEASIBILITY_BOOLEAN = "FEASIBILITY_BOOLEAN"
    PERFORMANCE_VALUE = "PERFORMANCE_VALUE"


class DimensionTypes(object):
    WEIGHT = ["Weight"]
    VOLUME = ["Volume"]
    HEIGHT = ["Height"]
    JUSTIEREN = ["Justieren"]


#-------META MODEl CLASSES---------------
class GenericThing(object):
    def __init__(self, id, name, type):
        self.id = id
        self.type = type
        self.name = name
        self.state = State.IDLE

    def set_completed(self):
        self.state = State.COMPLETED

    def start(self, time):
        self.startTime = time
        self.state = State.INPROGRESS


class AAS(GenericThing):
    pass


class Component(GenericThing):
    def __init__(self, id, name, type, building_element=[]):
        GenericThing.__init__(self, id, name, type)
        self.building_element = building_element


class Project(GenericThing):
    def __init__(self, id, name, AAS, ResourceAAS):
        GenericThing.__init__(self, id, name, "List")
        self.BuildingElementList = AAS
        self.resource_list = ResourceAAS

    def uncompleted_elements_remain(self):
        trueList = []
        for element in self.BuildingElementList:
            if element.state == State.COMPLETED:
                trueList.append(element)
        if len(trueList) == len(self.BuildingElementList):
            return False
        else:
            return True

    def get_all_transport_ressources(self):
        transport_resource = []
        for ressource in self.resource_list:
            if isinstance(ressource, self.resource_list[0].__class__): #nicht schön gelöst, was ist wenn erste ressource nicht transport ist
                transport_resource.append(ressource)
        return transport_resource

    def get_all_activitys_of_kind(self, instance):
        all_activities_of_a_kind = []
        for building_element in self.BuildingElementList:
            for activity in building_element.reference_process.activities:
                if isinstance(activity, instance):
                    all_activities_of_a_kind.append(activity)
        return all_activities_of_a_kind


class Measure():
    def __init__(self, value=0, dimensionName=None, dimensionUnit=None, valueRange=[0, 1], dataType="Integer"):
        self.value = value
        self.dimensionName = dimensionName
        self.dimensionUnit = dimensionUnit
        self.valueRange = valueRange
        self.dataType = dataType

    def setValue(self, val):
        self.value = val

    def __str__(self):
        return "Parameter: value=%d, dimensionName=%s, dimensionUnit=%s, valueRange=%s, dataType=%s" % (
        self.value, self.dimensionName, self.dimensionUnit, self.valueRange, self.dataType)


class Parameter(GenericThing):
    def __init__(self, id, dimensionName=None, dimensionUnit=None, dataType="Integer", capabilityType=None):
        GenericThing.__init__(self, id, dimensionName, dataType)
        self.dimensionUnit = dimensionUnit
        self.capabilityType = capabilityType

    def __str__(self):
        return "Parameter: value=%d, dimensionName=%s, dimensionUnit=%s, valueRange=%s, dataType=%s" % (
            self.value, self.name, self.dimensionUnit, self.dataType)


class ParameterFeasibilityQuantitative(Parameter):
    def __init__(self, id, dimension_name, dimension_unit, value_range, value):
        Parameter.__init__(self, id, dimension_name, dimension_unit)
        self.value_range = value_range
        self.value = value


class ParameterPerformanceValue(Parameter):
    def __init__(self, id, dimension_name, dimension_unit, value):
        Parameter.__init__(self, id, dimension_name, dimension_unit)
        self.value = value


class Weight(ParameterFeasibilityQuantitative):
    def __init__(self, dimensionName, dimensionUnit, valueRange=None, value=None):
        ParameterFeasibilityQuantitative.__init__(self, "Par_weight", dimensionName, dimensionUnit, valueRange, value)


class Volume(ParameterFeasibilityQuantitative):
    def __init__(self, dimensionName, dimensionUnit, valueRange=None, value=None):
        ParameterFeasibilityQuantitative.__init__(self, "Par_volume", dimensionName, dimensionUnit, valueRange, value)


class Height(ParameterFeasibilityQuantitative):
    def __init__(self, dimensionName, dimensionUnit, valueRange=None, value=None):
        ParameterFeasibilityQuantitative.__init__(self, "Par_height", dimensionName, dimensionUnit, valueRange, value)


class PerfVolume(ParameterPerformanceValue):
    def __init__(self, dimensionName, dimensionUnit, value):
        ParameterPerformanceValue.__init__(self, "Par_volume_performance", dimensionName, dimensionUnit, value)


class Velocity(ParameterPerformanceValue):
    def __init__(self, dimensionName, dimensionUnit, value):
        ParameterPerformanceValue.__init__(self, "Velocity_performance", dimensionName, dimensionUnit, value)


class Variable(GenericThing):
    pass


#--------Building Element Classes ---------------
'''
class Project(GenericThing):
    def __init__(self, id, name, buildingElementAASList):
        GenericThing.__init__(self, id, name, "List")
        self.buildingElementAASList = buildingElementAASList

    def uncompleted_elements_remain(self):
        trueList = []
        for element in self.buildingElementAASList:
            if element.state == State.COMPLETED:
                trueList.append(element)
        if len(trueList) == len(self.buildingElementAASList):
            return False
        else:
            return True
'''



class BuildingElementAAS(AAS):
    in_Right_Position = 0  # if Element is in right Postion = 1

    def __init__(self, id, name, type, parameters=[]):
        AAS.__init__(self, id, name, type)
        self.variables = []
        self.predecessors = []
        self.parameters = parameters
        self.set_reference_process()

    def set_reference_process(self):
        if self.type == "ifcSlab":
            self.reference_process = IfcSlabProcess(self.id, self.parameters, self)
        elif self.type == "ifcColumn":
            self.reference_process = IfcColumnProcess(self.id, self.parameters, self)
        elif self.type == "ifcWall":
            self.reference_process = IfcWallProcess(self.id, self.parameters, self)
        elif self.type == "ifcMember":
            self.reference_process = IfcMemberProcess(self.id, self.parameters, self)
        elif self.type == "ifcFooting":
            self.reference_process = IfcFootingProcess(self.id, self.parameters, self)
        elif self.type == "ifcBeam":
            self.reference_process = IfcBeamProcess(self.id, self.parameters, self)
        else:
            logging.error('Could not match reference type: ', self.type)

    def possible_start_assembly(self):
        trueList = []
        if self.state == State.INPROGRESS:
            return False
        if self.state == State.INPOSITION:
            for predecessors in self.predecessors:
                if predecessors.state == State.COMPLETED:
                    trueList.append("true")
            if len(trueList) != len(self.predecessors):
                return False
            return True

    def possible_start_transport(self):
        trueList = []
        if self.state != State.IDLE:
            return False
        for predecessors in self.predecessors:
            if predecessors.state != State.IDLE and predecessors.state != State.WAITING:
                trueList.append("true")
        if len(trueList) != len(self.predecessors):
            return False
        return True

    def __str__(self):
        return self.id


# ----- Process Classes -----------
class ReferenceProcess(Component):
    def get_next_activity(self, actualActivity):
        trueActivity = False
        for activity in self.activities:
            if trueActivity:
                return activity
            if activity == actualActivity:
                trueActivity = True

    def get_all_tranport_activities(self):
        list_of_transport_activities = []
        for activity in self.activities:
            if isinstance(activity, TransportActivity):
                list_of_transport_activities.append(activity)
        return list_of_transport_activities

    def get_all_assembly_activities(self):
        list_of_assembly_activities = []
        for activity in self.activities:
            if isinstance(activity, AssemblyActivity):
                list_of_assembly_activities.append(activity)
        return list_of_assembly_activities


class IfcSlabProcess(ReferenceProcess):
    def __init__(self, id, parameter, building_element):
        Component.__init__(self, id + "/RP_IFC_SLAB", "Reference process for ifcSlab", "IFC_SLAB", building_element)
        self.activities = [
            #LoadingActivity(self.id, parameter, building_element),
            TransportationActivity(self.id, parameter, building_element),
            #UnloadingActivity(self.id, weight_parameter, building_element),
            AdjustActivity(self.id, parameter, building_element),
            FixActivity(self.id, parameter, building_element)
        ]


class IfcColumnProcess(ReferenceProcess):
    def __init__(self, id, parameter, building_element):
        Component.__init__(self, id + "/RP_IFC_COLUMN", "Reference process for ifcColumn", "IFC_COLUMN", building_element)
        self.activities = [
            #LoadingActivity(self.id, parameter, self.building_element),
            TransportationActivity(self.id, parameter, self.building_element),
            #UnloadingActivity(self.id, parameter, self.building_element),
            #AdjustActivity(self.id, parameter, self.building_element),
            #FixActivity(self.id, parameter, self.building_element),
            FormActivity(self.id, parameter, building_element),
            ReinforceActivity(self.id, parameter, building_element),
            ConcreteActivity(self.id, parameter, building_element)
        ]


class IfcWallProcess(ReferenceProcess):
    def __init__(self, id, parameter, building_element):
        Component.__init__(self, id + "/RP_IFC_WALL", "Reference process for ifcWall", "IFC_WALL", building_element)
        self.activities = [
            #LoadingActivity(self.id, parameter, self.building_element),
            TransportationActivity(self.id, parameter, self.building_element),
            #UnloadingActivity(self.id, parameter, self.building_element),
            AdjustActivity(self.id, parameter, self.building_element),
            FixActivity(self.id, parameter, self.building_element)
        ]


class IfcMemberProcess(ReferenceProcess):
    def __init__(self, id, parameter, building_element):
        Component.__init__(self, id + "/RP_IFC_SLAB", "Reference process for ifcSlab", "IFC_SLAB", building_element)
        self.activities = [
            #LoadingActivity(self.id, parameter, building_element),
            TransportationActivity(self.id, parameter, building_element),
            #UnloadingActivity(self.id, weight_parameter, building_element),
            # AdjustActivity(self.id, parameter, self.building_element),
            # FixActivity(self.id, parameter, self.building_element),
            FormActivity(self.id, parameter, building_element),
            ReinforceActivity(self.id, parameter, building_element),
            ConcreteActivity(self.id, parameter, building_element)
        ]


class IfcBeamProcess(ReferenceProcess):
    def __init__(self, id, parameter, building_element):
        Component.__init__(self, id + "/RP_IFC_SLAB", "Reference process for ifcSlab", "IFC_SLAB", building_element)
        self.activities = [
            #LoadingActivity(self.id, parameter, building_element),
            TransportationActivity(self.id, parameter, building_element),
            #UnloadingActivity(self.id, weight_parameter, building_element),
            PositioningActivity(self.id, parameter, building_element),
            AdjustActivity(self.id, parameter, self.building_element),
            FixActivity(self.id, parameter, self.building_element),
            EndAssemblyActivity(self.id, parameter, building_element)
        ]


class IfcFootingProcess(ReferenceProcess):
    def __init__(self, id, parameter, building_element):
        Component.__init__(self, id + "/RP_IFC_SLAB", "Reference process for ifcSlab", "IFC_SLAB", building_element)
        self.activities = [
            #LoadingActivity(self.id, parameter, building_element),
            TransportationActivity(self.id, parameter, building_element),
            #UnloadingActivity(self.id, parameter, building_element),
            #AdjustActivity(self.id, parameter, building_element),
            #FixActivity(self.id, parameter, building_element)
            FormActivity(self.id, parameter, building_element),
            ReinforceActivity(self.id, parameter, building_element),
            ConcreteActivity(self.id, parameter, building_element)
        ]


# ---- Action Classes --------
class Activity(Component):
    capabilities = []
    endTime = 1000000
    waitTime = -100
    startTime = 1000000

    def set_duration(self):
        mainPerformance = 0
        parameterActivity = self.capabilities[0].get_parameters_by_type(ParameterFeasibilityQuantitative)
        for resource in self.allocatedResources:
            parameterResource = resource[2].get_parameters_by_type(ParameterPerformanceValue)
            if mainPerformance < parameterResource[0].value:
                mainPerformance = parameterResource[0].value
        self.duration = math.ceil(parameterActivity[0].value / mainPerformance)

    def set_end_time(self):
        self.endTime = self.startTime+self.duration

    def set_used_resource(self, resources):
        self.allocatedResources.append(resources)

    def get_end_time(self):
        return self.endTime

    def set_wait_time(self):
        self.waitTime = 100000
        for bussyResource in self.capabilities[0].bussyResourcen:
            if self.waitTime > bussyResource[0].get_bussy_time():
                self.waitTime = bussyResource[0].get_bussy_time()
        self.state = State.WAITING


class TransportActivity(Activity):
    def __init__(self, id, weight_parameters):
        self.id = id + "TA/"


    def start_activity_transport(self, time):
        self.startTime = time
        self.state = State.TRANSPORT


class AssemblyActivity(Activity):
    def __init__(self, id, parameter):
        self.id = id + "AA/"
        self.activities = [
            AdjustActivity(self.id, parameter),
            FixActivity(self.id, parameter)
        ]

    def start_activity_assembly(self, time):
        self.startTime = time
        self.state = State.INPROGRESS
        self.building_element.reference_process.state = State.INPROGRESS

    def set_duration(self):
        mainPerformance = 0
        parameterActivity = self.capabilities[0].get_parameters_by_type(ParameterPerformanceValue)
        for resource in self.allocatedResources:
            parameterResource = resource[2].get_parameters_by_type(ParameterPerformanceValue)
            if mainPerformance < parameterResource[0].value:
                mainPerformance = parameterResource[0].value
        self.duration = math.ceil(parameterActivity[0].value / mainPerformance)


class AdjustActivity(AssemblyActivity):
    def __init__(self, id, parameters, building_element):
        Component.__init__(self, id + '/AC_Adjust', "Adjust Activity", "ADJUST", building_element)
        self.capabilities = [AdjustCapability(self.id, "adjust capability", parameters)]
        self.allocatedResources = []


class FixActivity(AssemblyActivity):
    def __init__(self, id, parameters, building_element):
        Component.__init__(self, id + '/Fix', "Fix Activity", "FIX", building_element)
        self.capabilities = [FixCapability(self.id, "fix capability", parameters)]
        self.allocatedResources = []


class FormActivity(AssemblyActivity):
    def __init__(self, id, parameters, building_element):
        Component.__init__(self, id + '/Form', "Form Activity", "FORM", building_element)
        self.capabilities = [
                                PositioningCapability(self.id, "Positioning capability", parameters),
                                AssemblyCapability(self.id, "Assembly capability", parameters)
                            ]
        self.allocatedResources = []


class EndAssemblyActivity(AssemblyActivity):
    def __init__(self, id, parameters, building_element):
        Component.__init__(self, id + '/EndAssemblyActivity', "End Assembly Activity", "ENDASSEMBLY", building_element)
        self.capabilities = [
                                FixCapability(self.id, "fix capability", parameters)
                            ]
        self.allocatedResources = []


class PositioningActivity(AssemblyActivity):
    def __init__(self, id, parameters, building_element):
        Component.__init__(self, id + '/Positioning', "Positioning Activity", "POSITIONING", building_element)
        self.capabilities = [
                                PositioningCapability(self.id, "Positioning capability", parameters),
                            ]
        self.allocatedResources = []


class ReinforceActivity(AssemblyActivity):
    def __init__(self, id, parameters, building_element):
        Component.__init__(self, id + '/Reinforce', "Reinforce Activity", "REINFORCE", building_element)
        self.capabilities = [
            PositioningCapability(self.id, "Positioning capability", parameters),
            AssemblyCapability(self.id, "Assembly capability", parameters)
        ]
        self.allocatedResources = []


class ConcreteActivity(AssemblyActivity):
    def __init__(self, id, parameters, building_element):
        Component.__init__(self, id + '/Concrete', "Concrete Activity", "CONCRETE", building_element)
        self.capabilities = [
            PositioningCapability(self.id, "Positioning capability", parameters),
            ShakingCapability(self.id, "Shaking capability", parameters)
        ]
        self.allocatedResources = []


class LoadingActivity(TransportActivity):
    def __init__(self, id, parameters, building_element):
        Component.__init__(self, id + '/Loading', "Loading Activity", "LOADING", building_element)
        self.capabilities = [TransportCapability(self.id, "transport capability", parameters)]
        self.allocatedResources = []


class TransportationActivity(TransportActivity):
    def __init__(self, id, parameters, building_element):
        Component.__init__(self, id + '/Transportation', "Transportation Activity", "TRANSPORTATION", building_element)
        self.capabilities = [TransportCapability(self.id, "transport capability", parameters)]
        self.allocatedResources = []
        self.transport_location = []


class UnloadingActivity(TransportActivity):
    def __init__(self, id, parameters, building_element):
        Component.__init__(self, id + '/Unloading', "Unloading Activity", "UNLOADING", building_element)
        self.capabilities = [TransportCapability(self.id, "transport capability", parameters)]
        self.allocatedResources = []


class RessourceApproachActivity(TransportActivity):
    def __init__(self, id, parameters, building_element):
        Component.__init__(self, id + '/Approach', "Resource Approach Activity", "APPROACH", building_element)
        self.capabilities = [TransportCapability(self.id, "transport capability", parameters)]
        self.allocatedResources = []


# -------Resource Classes ---------
class ResourceAAS(AAS):
    currentSetup = 0
    location = Location.MACHINERY_STORAGE
    releaseTime = 0
    usedTime = []

    def __init__(self, id , type, name, setups):
        GenericThing.__init__(self, id, name, type)
        self.setups = setups

    def assign_tool(self, tool):
        self.tool = tool

    def __str__(self):
        return self.id

    def seize(self, activity):
        bussyTime = []
        self.state = State.BUSY
        self.releaseTime = activity.endTime
        ResourceAAS.usedTime.append([self.id, activity.startTime, activity.endTime])
        for objects in ResourceAAS.usedTime:
            if self.id == objects[0]:
                objects[0] = State.BUSY
                bussyTime.append(objects)
        self.usedTime = bussyTime
        self.releaseTime = self.usedTime[-1][-1]

    def release(self):
        self.state = State.IDLE
        self.releaseTime = 0

    def get_bussy_time(self):
        return self.releaseTime

    def change_setup(self, setup):
        self.currentSetup = setup

    def get_current_setup(self):
        return self.setups[self.currentSetup].id


class TransportResourceAAS(ResourceAAS):
    def __init__(self, id, type, name, setups):
        ResourceAAS.__init__(self, id, type, name, setups)


class WorkerResourceAAS(ResourceAAS):
    def __init__(self, id, type, name, setups):
        ResourceAAS.__init__(self, id, type, name, setups)


class CraneDriverResourceAAS(WorkerResourceAAS):
    def __init__(self, id, type, name, setup):
        super().__init__(self, id, type, name, setup)


class AssemblyWorkerResourceAAS(WorkerResourceAAS):
    def __init__(self, id, type, name, setup):
        super().__init__(self, id, type, name, setup)


class Setup(Component):
    def __init__(self, id, type, name, capabilities):
        super().__init__(self, id, type, name)
        self.capabilities = capabilities

    def __str__(self):
        return self.id

    def list_capabilities_of_setup(self):
        myCapabilities = []
        for capability in self.capabilities:
            myCapabilities.append(capability)
        return myCapabilities


# ----- Capability Classes ---------
class Capability(Component):
    def __init__(self, id, name="default name.",  parameters=[], description="Default.", measures=[]):
        Component.__init__(self, id+"/Capability", name, "capability")
        self.description = description
        self.parameters = parameters

    def list_parameter_dimension_names(self):
        myList = []
        for parameter in self.parameters:
            myList.append(parameter.dimensionName)
        return myList

    def get_parameters_by_type(self, parameter_type):
        myList = []
        for parameter in self.parameters:
            if isinstance(parameter, parameter_type):
                myList.append(parameter)
        return myList

    def __str__(self):
        return self.id

    def get_best_resource(self, resourceList):
        performanceValue = 0
        bestResource = []
        for resources in resourceList:  # with resources the duration could be calculated
            parameterList = resources[2].get_parameters_by_type(ParameterPerformanceValue)
            for parameter in parameterList:
                if parameter.dimensionUnit == "t/h" and parameter.value > performanceValue:
                    performanceValue = parameter.value
                    bestResource = resources
        return bestResource


class AdjustCapability(Capability):
    def __init__(self, id, name="default name.", parameters=[], description="Default.", measures=[]):
        self.id = id+"/AdjustCapability"
        self.name = name
        self.description = description
        perf_parameter = []
        for parameter in parameters:
            if isinstance(parameter, ParameterPerformanceValue):
                perf_parameter.append(parameter)
        self.parameters = perf_parameter


class FixCapability(Capability):
    def __init__(self, id,  name="default name.",  parameters=[],description="Default.", measures=[]):
        self.id = id+"/FixCapability"
        self.name = name
        self.description = description
        perf_parameter = []
        for parameter in parameters:
            if isinstance(parameter, ParameterPerformanceValue):
                perf_parameter.append(parameter)
        self.parameters = perf_parameter


class TransportCapability(Capability):
    def __init__(self, id, name="default name.", parameters=[], description="Default.",measures=[]):
        self.id = id+"/TransportCapability"
        self.name = name
        self.description = description
        self.parameters = parameters


class PositioningCapability(Capability):
    def __init__(self, id, name="default name.", parameters=[], description="Default.",measures=[]):
        self.id = id+"/PositioningCapability"
        self.name = name
        self.description = description
        self.parameters = parameters


class AssemblyCapability(Capability):
    def __init__(self, id, name="default name.", parameters=[], description="Default.",measures=[]):
        self.id = id+"/AssemblyCapability"
        self.name = name
        self.description = description
        perf_parameter = []
        for parameter in parameters:
            if isinstance(parameter, ParameterPerformanceValue):
                perf_parameter.append(parameter)
        self.parameters = perf_parameter


class ShakingCapability(Capability):
    def __init__(self, id, name="default name.", parameters=[], description="Default.",measures=[]):
        self.id = id+"/ShakingCapability"
        self.name = name
        self.description = description
        perf_parameter = []
        for parameter in parameters:
            if isinstance(parameter, ParameterPerformanceValue):
                perf_parameter.append(parameter)
        self.parameters = perf_parameter


class CraneDrivingCapability(Capability):
    pass

