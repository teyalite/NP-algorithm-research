from solutions import BruteForce, DynamicProgramming, Approximation
from test import favorite_test_case

approximation = Approximation(favorite_test_case[0], favorite_test_case[1].copy())
brute_force = BruteForce(favorite_test_case[0], favorite_test_case[1].copy())
dynamic_programming = DynamicProgramming(favorite_test_case[0], favorite_test_case[1].copy())
print(approximation.solution())
print(brute_force.solution())
print(dynamic_programming.solution())
