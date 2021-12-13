import os

"""Your goal is to find the number of distinct paths that start at start, end at
end, and don't visit small caves more than once."""

# Settings
path_data = "day_12.txt"

# Data
input = open(path_data).readlines()
input = [e.strip() for e in input]
input = [e.split("-") for e in input]
input = [*input, *[e[::-1] for e in input]]

# Create graph
nodes = {}
for a, b, in input:
    l = nodes.get(a, [])
    l.append(b)
    nodes[a] = l


def route(path, max_count):
    paths = 0 # []
    # print(path)
    options = nodes[path[-1]]
    for o in options:
        if o == "start":
            continue
        elif o == "end":
            new_path = path.copy()
            new_path.append(o)
            paths = paths + 1 #.append(new_path)
        elif o.islower():
            local_max = max_count
            if "small_cave_visited" in path:
                local_max = 1
            if path.count(o) >= local_max:
                continue
            else:
                new_path = path.copy()
                if path.count(o) == 1:
                    new_path.append("small_cave_visited")
                new_path.append(o)
                new_paths = route(new_path, max_count)
                paths = paths + new_paths # .extend(new_paths)
        elif o.isupper():
            new_path = path.copy()
            new_path.append(o)
            new_paths = route(new_path, max_count)
            paths = paths + new_paths # .extend(new_paths)
        else:
            raise ValueError()
    return paths


# paths = route(["start"], 1)
# print(paths)
# # print(len(paths))

paths = route(["start"], 2)
print(paths)
# print(len(paths))
