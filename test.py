favorite_test_case = [(0, 1, 4), (1, 2, 2), (2, 3, 5), (1, 3, 1), (3, 0, 3), (2, 0, 1)]


# generate a graph randomly
def generate_test_case():
    return favorite_test_case


# generate random graphs
def generate_test_cases():
    test_cases = [favorite_test_case]
    for _ in range(15):
        test_cases.append(generate_test_case())

    return test_cases


# run tests
def run_tests():
    test_inputs = generate_test_cases()
    print("--Run tests--")
    print(test_inputs)


# if it's main module then run tests
if __name__ == "__main__":
    run_tests()
