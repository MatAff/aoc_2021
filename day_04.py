import os

# Settings
path_data = "day_04.txt"

# Test Data
input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""".split("\n")
input = [e.strip() for e in input]


def get_numbers(input):
    return input[0].split(",")


def get_boards(input):
    nr = int(len(input[1:]) / 5)
    boards = []
    for i in range(nr):
        sub_lines = input[i * 5 + 1:i * 5 + 6]
        b = [[int(ee) for ee in e.split()] for e in sub_lines]
        boards.append(b)
    return boards


def check_number(boards, num):
    for b in boards:
        for r in range(5):
            for c in range(5):
                if b[r][c] == num:
                    b[r][c] = -1
    return boards


def check_bingo(boards):
    winners = []
    non_winners = []
    for b in boards:
        if -5 in list(map(sum, b)):
            winners.append(b)
        elif -5 in list(map(sum, list(zip(*b)))):
            winners.append(b)
        else:
            non_winners.append(b)
    return winners, non_winners


def score(b):
    total = 0
    for row in b:
        for c in row:
            if c != -1:
                total = total + c
    return total


def func(input):
    numbers = get_numbers(input)
    boards = get_boards(input)

    for num in numbers:
        boards = check_number(boards, int(num))
        winners, non_winners = check_bingo(boards)
        if len(winners) > 0:
            print(winners)
            assert len(winners) == 1
            total = score(winners[0])
            break
    return total * int(num)


def func2(input):
    numbers = get_numbers(input)
    boards = get_boards(input)

    previous = []
    for num in numbers:
        boards = check_number(boards, int(num))
        winners, non_winners = check_bingo(boards)
        if len(non_winners) < 1:
            assert len(previous) == 1
            total = score(previous[0])
            break
        previous = non_winners
    return total * int(num)


def test_func():

    # Using globally defined test data
    
    exp = 4512
    exp2 = 1924

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
        input = [e for e in input if e != ""]

        print(func(input))
        print(func2(input))
