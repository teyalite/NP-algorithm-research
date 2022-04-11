from itertools import permutations
import time
import matplotlib.pyplot as plt
from solutions import BruteForce, DynamicProgramming, Approximation

brute_force = BruteForce([(0, 1, 4), (1, 2, 2), (2, 3, 5), (1, 3, 1), (3, 0, 3), (2, 0, 1)])
print(brute_force.solution())
brute_force.draw()
plt.show()
