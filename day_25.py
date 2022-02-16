
path = "./day_25.txt"

input = open(path).read().split("\n")
input = [e for e in input if e.strip() != ""]
input = [list(e) for e in input]
# print(input)

width = len(input[0])
height = len(input)
print(width, height)


def show():
    for i in input:
        print("".join(i))
    print("")


moved = True
step_count = 0
# show()
while moved:
    # print(step_count)
    step_count = step_count + 1
    moved = False
    for step in ["east", "south"]:
        new_input = [e.copy() for e in input]
        for r in range(height):
            for c in range(width):
                if step == "east":
                    if input[r][c] == ">":
                        rr = r
                        cc = (c + 1) % width
                        if input[rr][cc] == ".":
                            new_input[rr][cc] = ">"
                            new_input[r][c] = "."
                            moved = True
                if step == "south":
                    if input[r][c] == "v":
                        rr = (r + 1) % height
                        cc = c
                        if input[rr][cc] == ".":
                            new_input[rr][cc] = "v"
                            new_input[r][c] = "."
                            moved = True
        input = [e.copy() for e in new_input]
    # show()
    # if step_count == 60:
    #     break

print(step_count)


    
    