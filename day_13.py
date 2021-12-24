import os

# Settings
path_data = "day_13.txt"

# Test Data
input = open(path_data).readlines()
input = [e.strip() for e in input]

break_pos = input.index("")
dots = input[:break_pos]
instructions = input[(break_pos + 1):]
dots, instructions
dots = [[int(i) for i in dot.split(",")] for dot in dots]


def fold(val, fold_pos):
    if val < fold_pos:
        return val
    else:
        return 2 * fold_pos - val

def apply_instruction(dots, instruction):
    [axis, val] = instruction.split(" ")[2].split("=")
    list_pos_dict = {"x": 0, "y": 1}
    list_pos = list_pos_dict.get(axis)
    val = int(val)

    # Loop through dots and update
    for i, e in enumerate(dots):
        e[list_pos] = fold(e[list_pos], val)

    return dots

for instruction in instructions:
    dots = apply_instruction(dots, instruction)

max_r = 50
max_c = 10
points = []
for r in range(max_r):
    row = []
    for c in range(max_c):
        row.append(' ')
    points.append(row)

for dot in dots:
    points[dot[0]][dot[1]] = "8"

print(points)

list([''.join(e) for e in points][::-1])

# BLHFJPJF

# part one left over
count_dict = {}
for dot in dots:
    count_dict[1000*dot[0] + dot[1]] = 1

print(len(count_dict))