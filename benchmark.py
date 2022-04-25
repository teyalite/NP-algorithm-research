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
        test_case = generate_test_case(node)
        dynamic_programming = DynamicProgramming(test_case[0], test_case[1])
        brute_force = BruteForce(test_case[0], test_case[1])
        time_data[node] = (measure_time(brute_force.solution), measure_time(dynamic_programming.solution), 0)

    return time_data


# if it's main module then run tests
if __name__ == "__main__":
    print("solutions execution time")
    data = solutions_execution_time()
    for key in data:
        print(
            'number of nodes is {}\n     brute force: {}\n     dynamic programming: {}\n     approximation: {}\n\n'.
                format(key, data[key][0], data[key][1], data[key][2]))
