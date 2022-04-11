from networkx.algorithms.shortest_paths import weighted
from itertools import permutations
import time
import networkx as nx
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt


# input_graph is an array of adjacent nodes and their distance
# each element in the array is tuple (source, destination, distance)
# it returns a suitable dictionary for tsp
def build_graph(input_graph):
    graph = {}
    # loop through all tuples
    for element in input_graph:
        if element[0] in graph:
            graph[element[0]][element[1]] = element[2]
        else:
            graph[element[0]] = {element[1]: element[2]}
        # the graph is undirected, therefore the destination also will contain information about the source
        if element[1] in graph:
            graph[element[1]][element[0]] = element[2]
        else:
            graph[element[1]] = {element[0]: element[2]}

    return graph


# pair map key function.
# it returns a key for a map as the max + min of the provided pair
def map_key(source, destination):
    return str(max(source, destination)) + str(min(source, destination))


# Parent class with abstract methods, properties, and common class.
class TravellingSalesman:
    # The class will have properties as follows
    # graph: a dictionary containing information (nodes and distances)
    # input_graph: initial graph structure provided
    def __init__(self, input_graph):
        self.input_graph = input_graph
        self.graph = build_graph(input_graph)

    # abstract method to be implemented by all children.
    @abstractmethod
    def solution(self):
        pass

    # draw the graph with labels and weights.
    # the green colored path is going to be the shortest path.
    # path argument is the shortest path.
    def draw(self, path=()):
        networkx_graph = nx.Graph()
        # path map to make a fast existence check for an edge
        path_map = {}
        for index in range(len(path)):
            path_map[map_key(path[index], path[(index + 1) % len(path)])] = True

        for node in [*self.graph]:
            networkx_graph.add_node(node)
        for node in self.graph:
            for destination in self.graph[node]:
                color = "green" if map_key(node, destination) in path_map else "black"
                networkx_graph.add_edge(node, destination, color=color, weight=self.graph[node][destination])

        positions = nx.spring_layout(networkx_graph)
        labels = nx.get_edge_attributes(networkx_graph, 'weight')
        colors = nx.get_edge_attributes(networkx_graph, 'color').values()
        nx.draw(networkx_graph, positions, with_labels=True, edge_color=colors)
        nx.draw_networkx_edge_labels(networkx_graph, positions, edge_labels=labels, font_weight='bold', label_pos=0.6,
                                     font_color="red")
