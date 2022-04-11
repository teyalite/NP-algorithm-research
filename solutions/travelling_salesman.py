from networkx.algorithms.shortest_paths import weighted
from itertools import permutations
import time
import networkx as nx
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt


class TravellingSalesman:
    # The class will have properties as follows
    # directed: indicates whether the graph is directed(directed by default)
    # graph: a dictionary containing information (nodes and distances)
    def __init__(self, input_graph, undirected):
        self.input_graph = input_graph
        self.undirected = undirected
        self.graph = self._build_graph(input_graph)

    @abstractmethod
    def solution(self):
        pass

    # input_graph is an array of adjacent nodes and their distance
    # each element in the array is tuple (source, destination, distance)
    # it returns a suitable dictionary for tsp
    def _build_graph(self, input_graph):
        graph = {}
        # loop through all tuples
        for element in input_graph:
            if element[0] in graph:
                graph[element[0]][element[1]] = element[2]
            else:
                graph[element[0]] = {element[1]: element[2]}

            # if the graph is undirected the destination will contain information of the source
            if self.undirected:
                if element[1] in graph:
                    graph[element[1]][element[0]] = element[2]
                else:
                    graph[element[1]] = {element[0]: element[2]}

        return graph

    def draw(self):
        networkx_graph = nx.Graph()

        for node in [*self.graph]:
            networkx_graph.add_node(node)
        for node in self.graph:
            for destination in self.graph[node]:
                networkx_graph.add_edge(node, destination, color='b', weight=self.graph[node][destination])
        print('\n\n')
        nx.draw(networkx_graph, with_labels=True, font_weight='bold')
