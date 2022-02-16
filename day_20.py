# Settings
path_data = "day_20.txt"

# Test Data
input = open(path_data).readlines()
input = [e.strip() for e in input]
# print(input)

def show_image(image):
    for line in image:
        print("".join(line))

# Look up key
look_up_key = input[0]

# Image
image = input[2:]

# Add border
border = "." * 200
image = [border + e + border for e in image]
top = "." * len(image[0])
for i in range(200):
    image = [
        top, 
        *image,
        top, 
    ]

# show_image(image)

# Convert to list of list
image = [list(row) for row in image]

# Get size
width = len(image[0])
height = len(image)
print(width, height)

# Create look up
look_dict = {}
for i in range(512):
    num = i
    s = ""
    base = 256
    for j in range(9):
        if num >= base:
            s = s + "#"
            num = num - base
        else:
            s = s + "."
        base = base / 2
    look_dict[s] = look_up_key[i]
# print(look_dict)

def copy_image(image):
    return [e.copy() for e in image]


def apply_step(image):
    new_image = copy_image(image)
    for r in range(1, height - 1):
        for c in range(1, width - 1):
            s = image[r - 1][c - 1: c + 2]
            s = s + image[r - 0][c - 1: c + 2]
            s = s + image[r + 1][c - 1: c + 2]
            new_image[r][c] = look_dict[''.join(s)]
            if (r == 10) and (c==3):
                print(s)
    return new_image


for i in range(50):
    image = apply_step(image)
    
# show_image(image)

look_dict["........."]

def count_hash(image):
    total = 0
    border = 52
    for r in range(border, height - border):
        for c in range(border, width - border):
            if image[r][c] == "#":
                total = total + 1
    return total

print(count_hash(image))

sub_image = [e[0:52] for e in image[0:100]]
show_image(sub_image)