from networkx.algorithms.shortest_paths import weighted
from itertools import permutations
import time
import networkx as nx
from abc import abstractmethod
import matplotlib.pyplot as plt


# input_graph is an array of adjacent nodes and their distance
# each element in the array is tuple (source, destination, distance)
# it returns the adjacency matrix for the given graph
def adjacency_matrix(number_of_nodes, input_graph):
    matrix = [list()] * number_of_nodes
    for i in range(number_of_nodes):
        matrix[i] = [-1] * number_of_nodes
    # loop through all tuples
    for element in input_graph:
        matrix[element[0]][element[1]] = element[2]
        # the graph is undirected, therefore the destination also will contain information about the source
        matrix[element[1]][element[0]] = element[2]

    return matrix


# input_graph is an array of adjacent nodes and their distance
# each element in the array is tuple (source, destination, distance)
# it returns the adjacency list for the given graph
def adjacency_list(input_graph):
    adj_list = {}

    for element in input_graph:
        if element[0] not in adj_list:
            adj_list[element[0]] = [(element[1], element[2])]
        else:
            adj_list[element[0]].append((element[1], element[2]))
        # The graph is undirected therefore save the reverse relation
        if element[1] not in adj_list:
            adj_list[element[1]] = [(element[0], element[2])]
        else:
            adj_list[element[1]].append((element[0], element[2]))

    return adj_list


# path map to make a fast existence check for an edge
def get_path_map(path):
    path_map = {}
    for index in range(len(path)):
        path_map[map_key(path[index], path[(index + 1) % len(path)])] = True

    return path_map


# compare two given solutions
def are_equal(first, second):
    if first[0] != second[0]:
        return False
    first_map = get_path_map(first[1])
    second_map = get_path_map(second[1])
    for key in first_map:
        if key not in second_map:
            return False
    return True


# pair map key function.
# it returns a key for a map as the max, min of the provided pair
def map_key(source, destination):
    return max(source, destination), min(source, destination)


# Parent class with abstract methods, properties, and common class.
class TravellingSalesman:
    # The class will have properties as follows
    # graph: a dictionary containing information (nodes and distances)
    # input_graph: initial graph structure provided
    def __init__(self, number_of_nodes, input_graph):
        self.number_of_nodes = number_of_nodes
        self.input_graph = input_graph
        self.adjacency_matrix = adjacency_matrix(number_of_nodes, input_graph)
        self.adjacency_list = adjacency_list(input_graph)

    # abstract method to be implemented by all children.
    @abstractmethod
    def solution(self):
        pass

    # draw the graph with labels and weights.
    # the green colored path is going to be the shortest path.
    # path argument is the shortest path.
    def draw(self, path=()):
        networkx_graph = nx.Graph()

        path_map = get_path_map(path)

        for node in range(self.number_of_nodes):
            networkx_graph.add_node(node)
        for node in range(self.number_of_nodes):
            for destination in range(self.number_of_nodes):
                if self.adjacency_matrix[node][destination] == -1:
                    continue
                color = "green" if map_key(node, destination) in path_map else "gray"
                networkx_graph.add_edge(node, destination, color=color, weight=self.adjacency_matrix[node][destination])

        positions = nx.spring_layout(networkx_graph)
        labels = nx.get_edge_attributes(networkx_graph, 'weight')
        colors = nx.get_edge_attributes(networkx_graph, 'color').values()
        nx.draw(networkx_graph, positions, with_labels=True, edge_color=colors)
        nx.draw_networkx_edge_labels(networkx_graph, positions, edge_labels=labels, font_weight='bold', label_pos=0.6,
                                     font_color="red")

        plt.show()
