# -*- coding: utf-8 -*-
'''
import os
script_dir = os.path.dirname(__file__)
resources_path = os.path.join(script_dir, "../data/resources.json")
with open(resources_path, 'r') as fi:
    pass

print(fi)
'''

from pathlib import Path
import pandas as pd
import json

def importPrecedenceGraph(precedencePath, buildingElementPath):
    precedenceDf = pd.read_csv(precedencePath, header=None)
    buildingElementDf = pd.read_csv(buildingElementPath)
    precedenceDf.insert(0, 'name', buildingElementDf['name'])
    return precedenceDf

def getResourceCounts(resourceJsonPath):
    #Load JSON from Path
    path = Path(__file__).parent / resourceJsonPath
    with path.open() as f:
        resources = json.loads(f.read())
    
    #Extract element count for every resource type and put into array
    resourcesCount = []
    for element in resources:
        resourcesCount.append(element['count'])
    return resourcesCount


        
        