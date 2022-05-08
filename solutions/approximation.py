from .travelling_salesman import TravellingSalesman
import math


# Comparator used to find the element key in the queue
def comparator(obj, value):
    return obj['value'] == value


# Find index of an element in array
def find_index(array, element):
    for i in range(len(array)):
        if comparator(array[i], element):
            return i


# Find the minimum spanning tree using Prim's algorithm
def minimum_spanning_tree(adjacency_list, number_of_nodes):
    queue = [dict()] * number_of_nodes
    selected = [False] * number_of_nodes
    tree = {}

    for i in range(number_of_nodes):
        queue[i] = {"parent": None, "key": math.inf, "value": i}

    queue[0]["key"] = 0
    while len(queue) != 0:
        node = min(queue, key=lambda x: x["key"])
        queue.remove(min(queue, key=lambda x: x["key"]))
        selected[node["value"]] = node

        for element in adjacency_list[node["value"]]:
            node_index = find_index(queue, element[0])
            if (not selected[element[0]]) and element[1] < queue[node_index]['key']:
                queue[node_index]['parent'] = node['value']
                queue[node_index]['key'] = element[1]

        tree[node["value"]] = []
        if node["parent"] is not None:
            tree[node["parent"]].append(node["value"])

    return tree


# depth first search
def depth_first_search(tree, vertex=0, discovered=None):
    if discovered is None:
        discovered = [False] * len(tree)

    discovered[vertex] = True
    vertices = []
    for node in tree[vertex]:
        if not discovered[node]:
            vertices = depth_first_search(tree, node, discovered)

    return [vertex] + vertices


# path from depth first search
def path_from_dfs(path):
    selected = {}
    way = []
    for node in path:
        if node not in selected:
            way.append(node)
            selected[node] = 0
    return way


# Travelling salesman approximation solution class
class Approximation(TravellingSalesman):
    def __init__(self, number_of_nodes, input_graph):
        super().__init__(number_of_nodes, input_graph)

    # brute force
    # running time is O((n - 1)!)
    # solution return a pair (shortest, shortestHow)
    def solution(self):
        tree = minimum_spanning_tree(self.adjacency_list, self.number_of_nodes)
        # depth first search on the mst
        path = path_from_dfs(depth_first_search(tree))
        cost = 0
        for node in range(len(path)):
            cost += self.adjacency_matrix[path[node]][path[(node + 1) % len(path)]]
        return cost, tuple(path)
