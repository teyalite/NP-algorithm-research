from itertools import permutations, combinations
from .travelling_salesman import TravellingSalesman


# Travelling salesman brute force solution class
class DynamicProgramming(TravellingSalesman):
    def __init__(self, number_of_nodes, input_graph):
        super().__init__(number_of_nodes, input_graph)

    # dynamic programming solution
    # algorithm used here is the Held–Karp algorithm
    # running time is O((n^2)(2^n))
    # solution return a pair (shortest, shortestHow)
    def solution(self):
        # Maps each subset of the nodes to the cost to reach that subset, as well
        # as what node it passed before reaching this subset.
        # Node subsets are represented as set bits.
        subset_map = {}

        # Set transition cost from initial state
        for k in range(1, self.number_of_nodes):
            subset_map[(1 << k, k)] = (self.adjacency_matrix[0][k], 0)

        # Iterate subsets of increasing length and store intermediate results
        # in classic dynamic programming manner
        for subset_size in range(2, self.number_of_nodes):
            for subset in combinations(range(1, self.number_of_nodes), subset_size):
                # Set bits for all nodes in this subset
                bits = 0
                for bit in subset:
                    bits |= 1 << bit

                # Find the lowest cost to get to this subset
                for k in subset:
                    prev = bits & ~(1 << k)

                    res = []
                    for m in subset:
                        if m == 0 or m == k:
                            continue
                        res.append((subset_map[(prev, m)][0] + self.adjacency_matrix[m][k], m))
                    subset_map[(bits, k)] = min(res)

        # all bits but the least significant (the starting one)
        bits = (2 ** self.number_of_nodes - 1) - 1
        # optimal cost
        res = []
        for k in range(1, self.number_of_nodes):
            res.append((subset_map[(bits, k)][0] + self.adjacency_matrix[k][0], k))
        shortest, parent = min(res)

        # Backtrack bits to find the full path
        shortest_how = []
        for i in range(self.number_of_nodes - 1):
            shortest_how.append(parent)
            tmp_bits = bits & ~(1 << parent)
            _, parent = subset_map[(bits, parent)]
            bits = tmp_bits

        # Adding the starting node
        shortest_how.append(0)

        return shortest, tuple(shortest_how)
