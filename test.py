import unittest
from random import randrange
from termcolor import cprint
from solutions import BruteForce, DynamicProgramming, Approximation, are_equal

favorite_test_case = (4, [(0, 1, 4), (1, 2, 2), (2, 3, 5), (1, 3, 1), (3, 0, 3), (2, 0, 1)])
favorite_test_case_expect = (7, (3, 1, 2, 0))


# generate a graph randomly
def generate_test_case(number_of_nodes=randrange(3, 10)):
    test_case = []

    for source in range(number_of_nodes):
        for destination in range(source + 1, number_of_nodes):
            test_case.append((source, destination, randrange(1, 1000)))

    return number_of_nodes, test_case


# generate random graphs
def generate_test_cases():
    test_cases = [favorite_test_case]
    for _ in range(15):
        test_cases.append(generate_test_case())
    return test_cases


def run_single_test(test_case):
    brute_force = BruteForce(test_case[0], test_case[1].copy())
    dynamic_programming = DynamicProgramming(test_case[0], test_case[1].copy())
    approximation = Approximation(test_case[0], test_case[1].copy())

    brute_force_solution = brute_force.solution()
    dynamic_programming_solution = dynamic_programming.solution()
    approximation_solution = approximation.solution()

    return_value = False

    if not are_equal(brute_force_solution, dynamic_programming_solution):
        cprint("------ TEST FAILED: DYNAMIC PROGRAMMING -----", "red")
        cprint("Got: {}".format(dynamic_programming_solution), "red")
        cprint("Expected: {}".format(brute_force_solution), "cyan")
        return_value = True
    else:
        cprint("------ TEST PASSED: DYNAMIC PROGRAMMING -----", "green")

    if not are_equal(brute_force_solution, approximation_solution):
        cprint("------ TEST FAILED: APPROXIMATION -----", "red")
        cprint("Got: {}".format(approximation_solution), "red")
        cprint("Expected: {}".format(brute_force_solution), "cyan")
        return_value = True
    else:
        cprint("------ TEST PASSED: APPROXIMATION -----", "green")

    return 1 if return_value else 0


# run tests
def run_tests():
    cprint("------ RUNNING TESTS ------", "blue")
    test_inputs = generate_test_cases()
    failed = 0
    for test_case in test_inputs:
        failed += run_single_test(test_case)
    cprint("Total: {}, failed: {}, passed: {}".format(len(test_inputs), failed, len(test_inputs) - failed), "blue")


# if it's main module then run tests
if __name__ == "__main__":
    run_tests()
