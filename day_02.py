

def func(input, hor, dep):

    for e in input:
        split = e.strip().split(" ")
        print(split)
        command, val = split[0], int(split[1])
        if command == "forward":
            hor = hor + val
        elif command == "down":
            dep = dep + val
        elif command == "up":
            dep = dep - val
        else:
            raise ValueError("Invalid command")

        assert dep >= 0

    return hor * dep



def func2(input, hor, dep, aim):
    """ Instructions

    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
    It increases your horizontal position by X units.
    It increases your depth by your aim multiplied by X.
    """

    for e in input:
        split = e.strip().split(" ")
        print(split)
        command, val = split[0], int(split[1])
        if command == "forward":
            hor = hor + val
            dep = dep + (aim * val)
        elif command == "down":
            aim = aim + val
        elif command == "up":
            aim = aim - val
        else:
            raise ValueError("Invalid command")

        assert dep >= 0

    return hor * dep



def test_func():

    input = """forward 5
    down 5
    forward 8
    up 3
    down 8
    forward 2""".split("\n")

    hor, dep, aim = 0, 0, 0

    exp = 150
    exp2 = 900

    res = func(input, hor, dep)
    res2 = func2(input, hor, dep, aim)

    assert res == exp
    assert res2 == exp2


if __name__ == "__main__":

    test_func()

    # Load data and preprocess
    input = open("input.txt").readlines()
    input = [e.strip() for e in input]

    print(func(input, 0, 0))
    print(func2(input, 0, 0, 0))