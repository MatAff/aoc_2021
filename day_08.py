
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


def it(parts, solution):
    current_d = d.copy()
    known = list(set(solution))
    if None in known:
        known.remove(None)
    
    # Create combos
    combos = create_combos(known, [])
    combos.append("")
    # print(combos)

    made_progress = False
    for comb in combos:
        sol = solution.copy()
        par = parts.copy()
        cur_d = current_d.copy()
        ref_d = {k: v for k, v in zip(sol, par)}
        base_letters = ""
        ref_letters = ""
        for k in comb:
            base_letters = base_letters + d[k]
            ref_letters = ref_letters + ref_d[k]
        
        # removing characters from dict
        cur_d = remove_letters_dict(cur_d, base_letters)
        
        # removing related characters from parts
        par = remove_letters_list(par, ref_letters)

        # Check for found digits
        cur_d = {k: v for k, v in cur_d.items() if k not in known}
        # print(cur_d)
        current_len = {len(v): k for k, v in cur_d.items()}
        lengths = [len(v) for k, v in cur_d.items()]
        for i, e in enumerate(par):
            if sol[i] is None:
                if lengths.count(len(e)) == 1:
                    sol[i] = current_len[len(e)]
                    made_progress = True
        
        if made_progress:
            return par, sol, made_progress

    return parts, solution, made_progress


def solve(line):
    parts = line.replace("| ", "").split(" ")
    parts_original = parts.copy()
    solution = [None] * len(parts)

    running = True
    while running:
        parts, solution, made_progress = it(parts, solution)
        # print(parts, solution, made_progress, running)
        if None not in solution[-4:]:
            running = False
    
    # print(solution, parts_original)
    
    # Nine correction
    for i, (s, p) in enumerate(zip(solution, parts_original)):
        # print(s, p)
        if s == 5:
            if len(p) == 6:
                # print("Correcting")
                solution[i] = 9

    return solution[-4:]

# line = input[0]
sol_list = []
total = 0
for line in input:
    sol = solve(line)
    sol_list.append(sol)
    val = int(''.join([str(e) for e in sol]))
    total = total + val

print(sol_list)
print(total)

