
# Settings
path_data = "day_08.txt"

# Data
input = open(path_data).readlines()
input = [e.strip() for e in input]

d = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

d_len = {k: len(v) for k, v in d.items()}

rel_digit = [1, 4, 7, 8]
rev_len = {v: k for k, v in d_len.items() if k in rel_digit}

total = 0
for line in input:
    end = line.split(" | ")[1]
    parts = end.split(" ")
    for p in parts:
        if len(p) in rev_len.keys():
            print(p)
            total = total + 1
print(total)
