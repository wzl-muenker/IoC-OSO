import networkx as nx
import matplotlib.pyplot as plt

from src.application.discrete_time_engine import *
from src.utilities.communication_master import *

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return  text[len(prefix):]
    return text


def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.
    Licensed under Creative Commons Attribution-Share Alike

    If the graph is a tree this will return the positions to plot this in a
    hierarchical layout.

    G: the graph (must be a tree)

    root: the root node of current branch
    - if the tree is directed and this is not given,
      the root will be found and used
    - if the tree is directed and this is given, then
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given,
      then a random choice will be used.

    width: horizontal space allocated for this branch - avoids overlap with other branches

    vert_gap: gap between levels of hierarchy

    vert_loc: vertical location of root

    xcenter: horizontal location of root
    '''
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  # allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''

        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                     pos=pos, parent=root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)

def get_Resources_to_Activity(model, element_index, activity_index):
    print("Considered Building Element: " + str(model.building_element_list[element_index]))
    for parameter in model.building_element_list[element_index].parameters:
        print(parameter.id, parameter.value)
    print("Considered Activity: " + str(model.building_element_list[element_index].reference_process.activities[activity_index].id))
    print('\n')
    for capability in model.building_element_list[element_index].reference_process.activities[activity_index].capabilities:
        print(capability, "benötigt:")
        for parameter in capability.parameters:
            if isinstance(parameter, ParameterFeasibilityQuantitative):
                print(parameter.id, parameter.value)
        print('\n')
        capability.possible_resources = get_possible_resources_by_capability(model.resource_list, capability)
        print("Mögliche Ressourcen:")
        for options in capability.possible_resources:
            print(options[0].id, options[1].name)
            for parameter in options[2].parameters:
                if isinstance(parameter, ParameterFeasibilityQuantitative):
                    print(parameter.id, parameter.value_range)
        print('\n')
    print('\n')

def get_feasibility_tree_graph(model, building_element_index):
    G = nx.Graph()

    element = model.building_element_list[building_element_index]
    print(f"Considered building element | id: {element.id}, name: {element.name}")
    G.add_node(element.id, name=element.name, color='lightgray', label=element.id, subset=0)

    all_activities = element.reference_process.activities
    activities = []
    for activity in all_activities:
        if activity.state == 'IDLE':
            activities.append(activity)

    # Building Element Nodes
    for activity in activities:
        G.add_node(activity.id, name=activity.name, color='bisque', label=remove_prefix(activity.id, element.id), subset=1)
        G.add_edge(element.id, activity.id)

        for capability in activity.capabilities:
            G.add_node(capability.id, name=capability.name, color='bisque', label=remove_prefix(capability.id, activity.id), subset=2)
            G.add_edge(activity.id, capability.id)

            for parameter in capability.parameters:
                G.add_node((capability.id + "/" + parameter.id), name=parameter.name, color='bisque',
                           label="/" + parameter.id + ": " + str(parameter.value) + " " + str(parameter.dimensionUnit), subset=3)
                G.add_edge(capability.id, (capability.id + "/" + parameter.id))


    #Resources nodes
    for resource in model.resource_list:
        G.add_node(resource.id, name=resource.name, color='lightskyblue', label=resource.name, subset=8)

        for setup in resource.setups:
            G.add_node((resource.id + "/" + setup.name), name=setup.name, color='lightskyblue', label='/' + setup.name, subset=7)
            G.add_edge((resource.id + "/" + setup.name), resource.id)

            for offered_capability in setup.capabilities:
                G.add_node((resource.id + "/" + offered_capability.id), name=offered_capability.name, color='lightskyblue', label=offered_capability.id[4:], subset=6)
                G.add_edge((resource.id + "/" + offered_capability.id), (resource.id + "/" + setup.name))

                for offered_parameter in offered_capability.parameters:
                    try:
                        offered_parameter_label = offered_parameter.id + ": " + str(offered_parameter.value_range) + " " + str(offered_parameter.dimensionUnit)
                    except:
                        offered_parameter_label = offered_parameter.id + ": " + str(offered_parameter.value) + " " + str(
                            offered_parameter.dimensionUnit)
                    G.add_node(resource.id + "/" + offered_capability.id + "/" + offered_parameter.id, name=offered_parameter.name, color='lightskyblue', label=offered_parameter_label, subset=5)
                    G.add_edge((resource.id + "/" + offered_capability.id + "/" + offered_parameter.id), (resource.id + "/" + offered_capability.id))

    # Connections
    for activity in activities:
        for capability in activity.capabilities:
            possible_resources = get_possible_resources_by_capability(model.resource_list, capability)

            for needed_parameter in capability.parameters:
                for resource in possible_resources:
                    for offered_parameter in resource[2].parameters:
                        if (resource[0].id + "/" + resource[2].id + "/" + offered_parameter.id) in G:
                            if (offered_parameter.id) == (needed_parameter.id):
                                G.add_edge((capability.id + "/" + needed_parameter.id), (resource[0].id + "/" + resource[2].id + "/" + offered_parameter.id))
                        else:
                            print("Node not existing: ")
                            print((resource[0].id + "/" + resource[2].id + "/" + offered_parameter.id))

    att_labels = nx.get_node_attributes(G, 'label')
    att_colors = list(nx.get_node_attributes(G, 'color').values())


    #pos = hierarchy_pos(G, root=element.id)
    pos = nx.multipartite_layout(G, scale=1.2)
    #pos = nx.kamada_kawai_layout(G)
    nx.draw_networkx(G, pos=pos, with_labels=False, node_color=att_colors)
    text = nx.draw_networkx_labels(G, pos, font_size=8, labels=att_labels)
    for _, t in text.items():
        t.set_rotation(45)
    plt.show()
    #data = json_graph.tree_data(G, root=element.id)
    #return data