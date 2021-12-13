
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


def remove_letters_string(s, letters):
    if s is None:
        return s
    for l in letters:
        s = s.replace(l, "")
    return s


def remove_letters_dict(d, letters):
    return {k: remove_letters_string(v, letters) for k, v in d.items()}


def remove_letters_list(l, letters):
    return [remove_letters_string(e, letters) for e in l]
        

def create_combos(items, so_far):
    new_combos = []
    for pos, i in enumerate(items):
        extra = [*so_far, i]
        new_combos.append(extra)
        remaining = items[(pos + 1):]
        if len(remaining) > 0:
            new_combos.extend(create_combos(remaining, extra))
    return new_combos

# create_combos(["a", "b", "c"], [])


def it(parts, solution):
    current_d = d.copy()
    known = list(set(solution))
    known.remove(None)
    
    # Create combos
    combos = create_combos(known, [])
    combos.append("")
    print(combos)

    # This needs to move up
    made_progress = False
    for comb in combos:
        print(comb)
        sol = solution.copy()
        par = parts.copy()
        cur_d = current_d.copy()
        ref_d = {k: v for k, v in zip(sol, par)}
        base_letters = ""
        ref_letters = ""
        for k in known:
            print(k)
            base_letters = base_letters + d[k]
            ref_letters = ref_letters + ref_d[k]
            
        # removing characters from dict
        cur_d = remove_letters_dict(cur_d, base_letters)
        
        # removing related characters from parts
        par = remove_letters_list(par, ref_letters)

        # Check for found digits
        cur_d = {k: v for k, v in cur_d.items() if k not in known}
        current_len = {len(v): k for k, v in cur_d.items()}
        lengths = [len(v) for k, v in cur_d.items()]
        for i, e in enumerate(par):
            if lengths.count(len(e)) == 1:
                sol[i] = current_len[len(e)]
                made_progress = True
        
        if made_progress:
            return par, sol, made_progress

        # # Recurvise
        # parts, solution = it(parts, solution)

    return parts, solution, made_progress


line = input[0]
# def solve(line):
parts = line.replace("| ", "").split(" ")
solution = [None] * len(parts)

parts, solution, made_progress = it(parts, solution)
print(parts, solution, made_progress)










list(zip(parts, solution))


# return 
solutions[-4:]






# on each iteration we have know and unknown digits as well as removed digits
mapping = {}
removed = []
# create_mapping(removed):
cleaned_d = d.copy()
for digit in removed:
    cleaned_d.pop(digit)
cleaned_d

lengths = [len(v) for k, v in cleaned_d.items()]

# after removing 
known = {k: v for k, v in cleaned_d.items() if len(v) == 1}
unknown = {k: v for k, v in cleaned_d.items() if len(v) > 1}




digits_removed = []
overall_mapping = {}
def create_mapping(d, digits_removed):
    print(d)
    print(digits_removed)
    len_mapping = {}
    for k, v in d.items():
        len_mapping[len(v)] = [*len_mapping.get(len(v), []), k]
    mapping = {}
    mapping["known"] = {k: v for k, v in len_mapping.items() if len(v) == 1}
    mapping["unknown"] = {k: v for k, v in len_mapping.items() if len(v) > 1}
    overall_key = "".join([str(i) for i in digits_removed])
    overall_mapping[overall_key] = mapping
    unknown_items = []
    for k, v in mapping["unknown"].items():
        unknown_items.extend(v)

    # Loop and add mapping for unknown items
    for known_key, known_val in mapping["known"].items():
        remove_digit = known_val[0]
        if remove_digit in digits_removed:
            continue
        # new_d = d.copy()
        # new_d.pop(remove_digit)
        new_d = {k: v for k, v in d.items() if k in unknown_items}
        
        
        
        
        create_mapping(new_d, [*digits_removed, remove_digit])

create_mapping(d, [])

known_val = [8]
    

# return mapping

{"": 0}


len_list = []




# def create_mapping(d, known, unknown):
len_mapping = {}
for k, v in d.items():
    len_mapping[len(v)] = [*len_mapping.get(len(v), []), k]
len_mapping["known"] = {k: v for k, v in len_mapping.items() if len(v) == 1}
len_mapping["unknown"] = {k: v for k, v in len_mapping.items() if len(v) > 1}


line = input[0]
print(line)
# def solve_line(line):
parts = line.replace("| ", "").split(" ")
parts



# loop through known values and remove characters
for k, v in known.items():
    print(k, v)
    for kk, vv in unknown.items():
        print(kk, vv)



# known = {}
# unknown = d.copy()
# # def create_mapping(d, known, unknown):
# len_mapping = {}
# for k, v in d.items():
#     len_mapping[len(v)] = [*len_mapping.get(len(v), []), k]





print(len_mapping)
known
unknown





len_mapping = {}
for k, v in d.items():
    l = len_mapping.get(len(v), [])
    l.append(k)
    len_mapping[len(v)] = l
print(len_mapping)


d_len = {k: len(v) for k, v in d.items()}
list(d_len.values())
len_map = {}


mapping = {}
d_len_dict = {k: len(v) for k, v in d.items()}
d_len_list = list(d_len_dict.values())
for k, v in d.items():
    if d_len_list.count(len(v)) == 1:
        mapping[len(d)]
for 







rel_digit = [1, 4, 7, 8]
rem_digit = [0, 2, 3, 4, 5, 9]

d_map = {}
for r in rel_digit:
    m_map = {}
    for m in rem_digit:
        v = d[m]
        for e in d[r]:
            v = v.replace(e, "")
        m_map[m] = v
    d_map[r] = m_map

d_map



end_parts = line.split(" | ")[1].split(" ")


d_len = {k: len(v) for k, v in d.items()}
print(d_len)

rev_len = {v: k for k, v in d_len.items() if k in rel_digit}
rev_len

total = 0
for line in input:
    end = line.split(" | ")[1]
    parts = end.split(" ")
    for p in parts:
        if len(p) in rev_len.keys():
            print(p)
            total = total + 1
print(total)