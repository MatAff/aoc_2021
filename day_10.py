import os

path_data = "day_10.txt"

input = open(path_data).readlines()
input = [e.strip() for e in input]

valid_dict = {e[0]: e[1] for e in ["[]","{}","()","<>"]}
val_dict = {")": 3, "]": 57, "}": 1197, ">": 25137}
comp_dict = {")": 1, "]": 2, "}": 3, ">": 4}
total = 0
comps = []
for line in input:
    print(line)
    q = []
    valid = True
    for c in line:
        if c in valid_dict.keys():
            q.append(c)
        else:
            prev = q.pop()
            if valid_dict[prev] != c:
                valid = False
                total = total + val_dict[c]
    print(valid)
    if len(q) > 0 and valid:
        print(line)
        print("".join(q))
        score = 0
        while len(q) > 0:
            c = q.pop()
            score = (score) * 5 + comp_dict[valid_dict[c]]
        comps.append(score)
print(total)
print(len(comps))
comps = sorted(comps)
print(comps)
print(sorted(comps)[(int(len(comps)/2)) + 0])

# 2857960589
# 2867760472