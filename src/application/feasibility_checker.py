# Auxiliary functions for feasiblity check

from src.IoC_OSO.class_models import *

def get_possible_resources_by_capability(resource_list, needed_capability):
    needed_parameters_quantitative = needed_capability.get_parameters_by_type(ParameterFeasibilityQuantitative)
    possibleRessources = []

    for resource in resource_list:
        for setup in resource.setups:
            for offered_capability in setup.capabilities:
                if isinstance(offered_capability,needed_capability.__class__):
                    offered_parameters_quantitative = offered_capability.get_parameters_by_type(ParameterFeasibilityQuantitative)

                    if quantitative_parameters_feasible(needed_parameters_quantitative, offered_parameters_quantitative):
                        setting = [resource, setup, offered_capability, offered_parameters_quantitative]
                        possibleRessources.append(setting)

    #TODO: return values are not resources but list of setting. Try to return only resources
    if possibleRessources:
        pass
    else:
        print("keine passende Ressource Vorhanden")
        return
    return possibleRessources

def quantitative_parameters_feasible(neededParameters, offeredParameters):
    trueList =[]
    for neededParameter in neededParameters:
        for offeredParameter in offeredParameters:
                if isinstance(offeredParameter, neededParameter.__class__):
                    if int(neededParameter.value) in range(offeredParameter.value_range[0], offeredParameter.value_range[1]):
                        trueList.append("true")
                        break
    if len(trueList) == len(neededParameters):
        return True
    else:
        return False
