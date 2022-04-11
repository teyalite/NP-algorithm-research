import time
from test import generate_test_case
from solutions import BruteForce, DynamicProgramming, Approximation


# Measure execution time of a function
def measure_time(function):
    starting_time = time.time()
    function()
    return time.time() - starting_time


# returns a list of tuple (brute_force, dynamic_programming, approximation solution
def solutions_execution_time():
    time_data = {}
    for node in range(2, 11):
        print(node)
        test_case = generate_test_case(node)
        print(len(test_case))
        brute_force = BruteForce(test_case[0], test_case[1])
        dynamic_programming = DynamicProgramming(test_case[0], test_case[1])
        time_data[node] = (measure_time(brute_force.solution), measure_time(dynamic_programming.solution), 0)

    return time_data


# if it's main module then run tests
if __name__ == "__main__":
    print("solutions_execution_time")
    data = solutions_execution_time()
    print(data)
