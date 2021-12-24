# Settings
path_data = "day_15.txt"

# Test Data
input = open(path_data).readlines()
input = [[int(c) for c in list(e.strip())] for e in input]
# print(input)

# Expand input
def update(line):
    return [i + 1 if i < 9 else 1 for i in line]


new_input = []
for line in input:
    new_line = line.copy()
    updated_line = line.copy()
    for i in range(4):
        updated_line = update(updated_line)
        new_line.extend(updated_line)
    new_input.append(new_line)
new_field = new_input.copy()
updated_section = new_input.copy()
for i in range(4):
    updated_section = [update(l) for l in updated_section]
    new_field.extend(updated_section)
input = new_field

# Get space
width = len(input[0])
height = len(input)
print(width, height)

# input[0][0:14]
# list(zip(*new_field))[0][0:14]
# for line in input:
#     print("".join([str(e) for e in line]))

paths = [{"nodes":[(0, 0)], "dist": 0, "visited": False}]
paths = sorted(paths, key=lambda d: d["dist"]) 

def get_neighbors(r, c):
    potentials = []
    for d in (-1, 1):
        potentials.append((r + d, c))
        potentials.append((r, c + d))
    return [p for p in potentials if (p[0] >= 0) and (p[0] < height) and (p[1] >= 0) and (p[1] < width)]

visited_paths = []
running = True
it_count = 0
max_count = 1000000
nodes_dists = {(0, 0): 0}
while running:
    paths = sorted(paths, key=lambda d: d["dist"] * -1) 
    found_path = False
    while found_path == False:
        base_path = paths.pop()
        # if base_path["visited"]:
        #     continue
        visited_paths.append(base_path)
        base_path["visited"] = True
        nodes = base_path["nodes"] 
        dist = base_path["dist"]
        r, c = nodes[-1]
        potentials = get_neighbors(r, c)
        potentials = [p for p in potentials if p not in nodes]
        potentials = [p for p in potentials if p not in nodes_dists.keys()]
        if len(potentials) > 0:
            found_path = True
            for p in potentials:
                new_nodes = nodes.copy()
                new_nones = new_nodes.append(p)
                new_dist = dist + input[p[0]][p[1]]
                nodes_dists[p] = new_dist
                if p == (height - 1, width - 1):
                    print("Success")
                    print(new_dist)
                    running = False
                paths.append({
                    "nodes": new_nodes,
                    "dist": new_dist,
                    "visited": False
                })
            break
    it_count = it_count + 1
    if it_count > max_count:
        running = False
print(paths[0])



# # Create min dist matrix
# risk_matrix = [[10**10 for c in row] for row in input]

# # Create path matrix
# risk = 0
# for r in range(height):
#     for c in range(width):
#         risk = risk + input[r][c]
#         risk_matrix[r][c] = risk








# def explore(r, c, risk):
#     if r < 0: return
#     if c < 0: return
#     if r >= height: return 
#     if c >= width: return 
#     new_risk = risk + input[r][c]
#     if new_risk < risk_matrix[r][c]:
#         risk_matrix[r][c]
#         # Also explore furter
#         explore(r - 1, c, risk)
#         explore(r + 1, c, risk)
#         explore(r, c - 1, risk)
#         explore(r, c + 1, risk)
#     else:
#         pass # Don't dig deeper

# explore(0, 0, 0)

# expected = 40
# print(risk_matrix[height - 1][width - 1])


# # Create the graph for easy traversing

# # Breadth or depth first graph algorithms

# # However there are too many paths to do this brute force

# # Instead we can keep track of the closest path to each point

# # We could even do this from both sides simultaneously

