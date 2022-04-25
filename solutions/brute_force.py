from itertools import permutations
from .travelling_salesman import TravellingSalesman


# Travelling salesman brute force solution class
class BruteForce(TravellingSalesman):
    def __init__(self, number_of_nodes, input_graph):
        super().__init__(number_of_nodes, input_graph)

    # brute force
    # running time is O(n!)
    # solution return a pair (shortest, shortestHow)
    def solution(self):
        # giving -1 as default value
        # shortest path value
        shortest = -1
        # shortest path
        shortest_how = ()
        # Explore all possible path
        for way in permutations(range(self.number_of_nodes)):
            current_cost = 0
            for index in range(len(way)):
                destination = way[(index + 1) % len(way)]
                source = way[index]
                if self.adjacency_matrix[source][destination] == - 1:
                    current_cost = -1
                    break
                else:
                    if current_cost >= 0:
                        current_cost += self.adjacency_matrix[source][destination]
            # change the shortest only if the path contains all nodes
            if current_cost >= 0:
                shortest = current_cost if (shortest < 0) else min(shortest, current_cost)
                if shortest == current_cost:
                    shortest_how = way

        return shortest, shortest_how
