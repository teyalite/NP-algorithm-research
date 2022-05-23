import unittest
from solutions import BruteForce, DynamicProgramming, Approximation, are_equal
from test import favorite_test_case, favorite_test_case_expect


class Test(unittest.TestCase):
    # Test brute force solution
    def test_brute_force(self):
        brute_force = BruteForce(favorite_test_case[0], favorite_test_case[1].copy())
        solution = brute_force.solution()
        self.assertTrue(are_equal(solution, favorite_test_case_expect), msg="Brute force test")

    # Test dynamic programming solution
    def test_dynamic_programming(self):
        dynamic_programming = DynamicProgramming(favorite_test_case[0], favorite_test_case[1].copy())
        solution = dynamic_programming.solution()
        self.assertTrue(are_equal(solution, favorite_test_case_expect), msg="Dynamic programming test")

    # Approximation solution test
    def test_approximation(self):
        approximation = Approximation(favorite_test_case[0], favorite_test_case[1].copy())
        solution = approximation.solution()
        self.assertTrue(are_equal(solution, favorite_test_case_expect), msg="Approximation test")


if __name__ == "__main__":
    unittest.main()
