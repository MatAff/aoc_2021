# --- Day 9: Smoke Basin ---

# These caves seem to be lava tubes. Parts are even still volcanically active; 
# small hydrothermal vents release smoke into the caves that slowly settles like rain.

# If you can model how the smoke flows through the caves, you might be able to 
# avoid it and be that much safer. The submarine generates a heightmap of the 
# floor of the nearby caves for you (your puzzle input).

# Smoke flows to the lowest point of the area it's in. For example, consider 
# the following heightmap:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# Each number corresponds to the height of a particular location, where 9 is the 
# highest and 0 is the lowest a location can be.

# Your first goal is to find the low points - the locations that are lower than 
# any of its adjacent locations. Most locations have four adjacent locations 
# (up, down, left, and right); locations on the edge or corner of the map have 
# three or two adjacent locations, respectively. (Diagonal locations do not 
# count as adjacent.)

# In the above example, there are four low points, all highlighted: two are in 
# the first row (a 1 and a 0), one is in the third row (a 5), and one is in the 
# bottom row (also a 5). All other locations on the heightmap have some lower 
# adjacent location, and so are not low points.

# The risk level of a low point is 1 plus its height. In the above example, the 
# risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels 
# of all low points in the heightmap is therefore 15.

# Find all of the low points on your heightmap. What is the sum of the risk 
# levels of all low points on your heightmap?


# Settings
path_data = "day_09.txt"

# Data
input = open(path_data).readlines()
input = [e.strip() for e in input]
input = [[int(i) for i in list(e)] for e in input]
input

height = len(input)
width = len(input[0])

def get_pos(r, c):
    if r < 0:
        return 999
    if c < 0:
        return 999
    try:
        return input[r][c]
    except:
        return 999


def is_low_point(ri, ci, val):
    for rd in (-1, 1):
        if get_pos(ri + rd, ci) <= val:
            return False
    for cd in (-1, 1):
        if get_pos(ri, ci + cd) <= val:
            return False
    return True

total = 0
for ri, row in enumerate(input):
    for ci, c in enumerate(row):
        if is_low_point(ri, ci, c):
            total = total + c + 1
print(total)

# --- Part Two ---
# Next, you need to find the largest basins so you know what areas are most 
# important to avoid.

# A basin is all locations that eventually flow downward to a single low point. 
# Therefore, every low point has a basin, although some basins are very small. 
# Locations of height 9 do not count as being in any basin, and all other 
# locations will always be part of exactly one basin.

# The size of a basin is the number of locations within the basin, including 
# the low point. The example above has four basins.


# Convert to categories
def clasify(c):
    if c == 9:
        return 9
    else:
        return 0


input = [[clasify(c) for c in row] for row in input]
input
# print(input)


def explore_basin(r, c):
    val = get_pos(r, c)
    if val > 0:
        return 0
    input[r][c] = 1
    total = 1
    for d in (-1, 1):
        total = total + explore_basin(r + d, c)
        total = total + explore_basin(r, c + d)
    return total


# Loop
total = 0
basin_sizes = []
for ri, row in enumerate(input):
    for ci, c in enumerate(row):
        if c == 0:
            print("found new basin", ri, ci)
            size = explore_basin(ri, ci)
            basin_sizes.append(size)
print(basin_sizes)
basin_sizes = sorted(basin_sizes)
print(basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1])
