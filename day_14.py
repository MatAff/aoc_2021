# --- Day 14: Extended Polymerization ---
# The incredible pressures at this depth are starting to put a strain on your 
# submarine. The submarine has polymerization equipment that would produce 
# suitable materials to reinforce the submarine, and the nearby volcanically-
# active caves should even have the necessary input elements in sufficient quantities.

# The submarine manual contains instructions for finding the optimal polymer 
# formula; specifically, it offers a polymer template and a list of pair 
# insertion rules (your puzzle input). You just need to work out what polymer 
# would result after repeating the pair insertion process a few times.

# For example:

# NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C
# The first line is the polymer template - this is the starting point of 
# the process.

# The following section defines the pair insertion rules. A rule like 
# AB -> C means that when elements A and B are immediately adjacent, 
# element C should be inserted between them. These insertions all happen s
# imultaneously.

# So, starting with the polymer template NNCB, the first step simultaneously 
# considers all three pairs:

# The first pair (NN) matches the rule NN -> C, so element C is inserted b
# etween the first N and the second N.
# The second pair (NC) matches the rule NC -> B, so element B is inserted 
# between the N and the C.
# The third pair (CB) matches the rule CB -> H, so element H is inserted 
# between the C and the B.
# Note that these pairs overlap: the second element of one pair is the 
# first element of the next pair. Also, because all pairs are considered 
# simultaneously, inserted elements are not considered to be part of a 
# pair until the next step.

# After the first step of this process, the polymer becomes NCNBCHB.

# Here are the results of a few steps using the above rules:

# Template:     NNCB
# After step 1: NCNBCHB
# After step 2: NBCCNBBBCBHCB
# After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
# After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
# This polymer grows quickly. After step 5, it has length 97; After step 10, 
# it has length 3073. After step 10, B occurs 1749 times, C occurs 298 times, 
# H occurs 161 times, and N occurs 865 times; taking the quantity of the most 
# common element (B, 1749) and subtracting the quantity of the least common 
# element (H, 161) produces 1749 - 161 = 1588.

# Apply 10 steps of pair insertion to the polymer template and find the most 
# and least common elements in the result. What do you get if you take the 
# quantity of the most common element and subtract the quantity of the least 
# common element?

d = {
    "CH": "B",
    "HH": "N",
    "CB": "H",
    "NH": "C",
    "HB": "C",
    "HC": "B",
    "HN": "C",
    "NN": "C",
    "BH": "H",
    "NC": "B",
    "NB": "B",
    "BN": "B",
    "BB": "N",
    "BC": "B",
    "CC": "N",
    "CN": "C",
}

s = "NNCB"

# Settings
path_data = "day_14.txt"

# Data
input = open(path_data).readlines()
input = [e.strip() for e in input]

s = input[0]

d = {}
for e in input[2:]:
    k, v = e.split(" -> ")
    d[k] = v

def update(s):
    ns = ""
    for a, b in zip(s[:-1], s[1:]):
        ns = ns + d[a + b]
    l = list(zip(s, ns + "x"))
    return ''.join([''.join(e) for e in l])[:-1]

for i in range(10):
    s = update(s)
# print(s)

max_val = 0
min_val = 10**10
for e in set(list(s)):
    c = s.count(e)
    max_val = max(max_val, c)
    min_val = min(min_val, c)
print(max_val - min_val)

# --- Part Two ---
# The resulting polymer isn't nearly strong enough to reinforce the submarine. 
# You'll need to run more steps of the pair insertion process; a total of 40 
# steps should do it.

# In the above example, the most common element is B (occurring 2192039569602 
# times) and the least common element is H (occurring 3849876073 times); 
# subtracting these produces 2188189693529.

# Apply 40 steps of pair insertion to the polymer template and find the most 
# and least common elements in the result. What do you get if you take the 
# quantity of the most common element and subtract the quantity of the least 
# common element?

s = input[0]
print(s)

max_depth = 40

# def dig(a, b, count_dict, depth):
#     if depth > max_depth:
#         return count_dict
#     n = d[a + b]
#     count_dict[n] = count_dict.get(n, 0) + 1
#     count_dict = dig(a, n, count_dict, depth + 1)
#     count_dict = dig(n, b, count_dict, depth + 1)
#     return count_dict

# count_dict = {}
# for a, b in zip(s[:-1], s[1:]):
#     print(a, end='')
#     count_dict[a] = count_dict.get(a, 0) + 1
#     count_dict[b] = count_dict.get(b, 0) + 1
#     count_dict = dig(a, b, count_dict, depth=1)
# print(max(count_dict.values()) - min(count_dict.values()))

def update(s):
    ns = ""
    for a, b in zip(s[:-1], s[1:]):
        ns = ns + d[a + b]
    l = list(zip(s, ns + "x"))
    return ''.join([''.join(e) for e in l])[:-1]

# %%time
def create_look_up(s):
    for i in range(20):
        s = update(s)
    return s

dd = {}
for k in d.keys():
    dd[k] = create_look_up(k)

letters = set(''.join(d.keys()))

def count_letters(s):
    count_dict = {}
    for e in letters:
        count_dict[e] = s.count(e)
    return count_dict

dd_count = {}
for k in d.keys():
    dd_count[k] = count_letters(dd[k][:-1]) # Exclude last letter

print(s)
count_dict = {}
for a, b in zip(s[:-1], s[1:]):
    print(a, end='')
    dd_s = dd[a + b]
    for c, e in zip(dd_s[:-1], dd_s[1:]):
        add_dict = dd_count[c + e]
        for l in letters:
            count_dict[l] = count_dict.get(l, 0) + add_dict.get(l, 0)
count_dict[s[-1]] = count_dict[s[-1]] + 1
print()
print(max(count_dict.values()) - min(count_dict.values()))



