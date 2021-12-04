import os

# Settings
path_data = "day_xx.txt"

# Test Data
input = """
""".split("\n")
input = [e.strip() for e in input]

def func(input):
    return None


def func2(input):
    return None


def test_func():

    # Using globally defined test data
    
    exp = None
    exp2 = None

    res = func(input)
    res2 = func2(input)

    if exp is not None:
        assert res == exp
    if exp is not None:
        assert res2 == exp2

if __name__ == "__main__":

    test_func()

    if os.path.exists(path_data):

        # Load data and preprocess
        input = open(path_data).readlines()
        input = [e.strip() for e in input]

        print(func(input))
        print(func2(input))