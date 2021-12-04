import os

# Settings
path_data = "day_03.txt"

# Test Data
input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".split("\n")
input = [e.strip() for e in input]


def det(l):
    return bool(sum(list(map(int, l))) / len(l) > 0.5)


def bin_to_dec(l):
    total = 0
    for i, v in enumerate(l[::-1]):
        total = total + 2**i * int(v)
    return total


def func(input):
    inv = list(zip(*input))
    gamma = list(map(det, inv))
    epsilon = [e == False for e in gamma]
    return bin_to_dec(gamma) * bin_to_dec(epsilon)


def func2(input):

    """To find oxygen generator rating, determine the most common value (0 or 1) 
    in the current bit position, and keep only numbers with that bit in that 
    position. If 0 and 1 are equally common, keep values with a 1 in the position 
    being considered."""

    pos = 0
    ox = input
    while len(ox) > 1:
        inv = list(zip(*ox))
        one = sum([int(e) for e in inv[pos]])
        if one >= (len(inv[pos]) / 2):
            cri = "1"
        else:
            cri = "0"
        ox = [e for e in ox if e[pos] == cri]
        pos = pos + 1
    ox = ox[0]


    pos = 0
    co = input
    while len(co) > 1:
        inv = list(zip(*co))
        one = sum([int(e) for e in inv[pos]])
        if one >= (len(inv[pos]) / 2):
            cri = "0"
        else:
            cri = "1"
        co = [e for e in co if e[pos] == cri]
        pos = pos + 1
    co = co[0]

    return bin_to_dec(ox) * bin_to_dec(co)


def test_func():

    # Using globally defined test data

    exp = 198
    exp2 = 230

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