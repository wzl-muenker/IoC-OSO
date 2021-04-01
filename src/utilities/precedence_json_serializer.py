from networkx.readwrite import json_graph
import json

def dump_json(G, file_name):
    data = json_graph.adjacency_data(G)
    with open(file_name, 'w') as f:
        json.dump(data, f)

def load_json(file_name):
    data = json.load(open(file_name))
    G = json_graph.adjacency_graph(data)
    return G


