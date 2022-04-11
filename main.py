from itertools import permutations
import time
import matplotlib.pyplot as plt
from solutions import BruteForce, DynamicProgramming, Approximation
from test import favorite_test_case

brute_force = BruteForce(favorite_test_case)
cost, path = brute_force.solution()
print(cost, path)
brute_force.draw(path)
plt.show()
