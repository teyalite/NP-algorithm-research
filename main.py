import matplotlib.pyplot as plt
from solutions import BruteForce, DynamicProgramming, Approximation
from test import favorite_test_case

brute_force = BruteForce(favorite_test_case[0], favorite_test_case[1])
dynamic_programming = DynamicProgramming(favorite_test_case[0], favorite_test_case[1])
cost, path = brute_force.solution()
print(cost, path)
print(dynamic_programming.solution())
brute_force.draw(path)
plt.show()
