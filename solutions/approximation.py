from itertools import permutations
from .travelling_salesman import TravellingSalesman


# Travelling salesman brute force solution class
class Approximation(TravellingSalesman):
    def __init__(self, input_graph, undirected=True):
        super().__init__(input_graph, undirected)

    # brute force
    # running time is O((n - 1)!)
    # solution return a pair (shortest, shortestHow)
    def solution(self):
        # giving -1 as default value
        # shortest path value
        shortest = -1
        # shortest path
        shortest_how = ()

        # Explore all possible path
        for way in permutations([*self.graph]):
            current_how = 0

            for index in range(len(way)):
                destination = way[(index + 1) % len(way)]
                if not (destination in (self.graph[way[index]])):
                    current_how = -1
                    break
                else:
                    if current_how >= 0:
                        current_how += self.graph[way[index]][destination]
            # change the shortest only if the path contains all nodes
            if current_how >= 0:
                shortest = current_how if (shortest < 0) else min(shortest, current_how)
                if shortest == current_how:
                    shortest_how = way

        return shortest, shortest_how
