import os

# Settings
path_data = "day_11.txt"

# Test Data
input = open(path_data).readlines()
input = [e.strip() for e in input]
input = [[int(i) for i in list(e)] for e in input]
input

size = 10
dir = [-1, 0, 1]


def add_one(ll):
    for ri, r in enumerate(ll):
        for ci, c in enumerate(r):
            ll[ri][ci] = ll[ri][ci] + 1


def check_flash(ll):
    flashes = 0
    something_flashed = True
    while something_flashed:
        something_flashed = False
        for ri, r in enumerate(ll):
            for ci, c in enumerate(r):
                if ll[ri][ci] > 9:
                    something_flashed = True
                    flashes = flashes + 1
                    ll[ri][ci] = -1
                    for rd in dir:
                        if ((ri + rd) >= 0) and ((ri + rd) < 10):
                            for cd in dir:
                                if ((ci + cd) >= 0) and ((ci + cd) < 10):
                                    if ll[ri+rd][ci+cd] != -1:
                                        ll[ri+rd][ci+cd] = ll[ri+rd][ci+cd] + 1
    return flashes 


def reset(ll):
    for ri, r in enumerate(ll):
        for ci, c in enumerate(r):
            if ll[ri][ci] == -1:
                ll[ri][ci] = 0


total = 0
for i in range(100):
    add_one(input)
    total = total + check_flash(input)
    reset(input)
print(total)

input = open(path_data).readlines()
input = [e.strip() for e in input]
input = [[int(i) for i in list(e)] for e in input]
input

for i in range(1000):
    add_one(input)
    flashes = check_flash(input)
    reset(input)
    if flashes == 100:
        print(input)
        print(i + 1)
        break
    

