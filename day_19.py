# Settings
path_data = "day_19.txt"

# Test Data
input = open(path_data).readlines()
input = [e.strip() for e in input]
# print(input)

# Process input
scanners = []
for line in input:
    if "scanner" in line:
        new_scanner = []
    elif line == "":
        scanners.append(new_scanner)
    else:
        new_scanner.append([int(e) for e in line.split(",")])
scanners.append(new_scanner)
# print(scanners)


def compute_dist(s, t):
    return ((s[0]-t[0])**2 + (s[1]-t[1])**2 + (s[2]-t[2])**2) ** 0.5
# compute_dist((0, 0, 0), (1, 1, 1))


def compute_distances(scanner):
    dist_dict = {}
    for i, source in enumerate(scanner):
        for j, target in enumerate(scanner):
            if i == j:
                break
            dist = compute_dist(source, target)
            if dist in dist_dict.keys():
                raise ValueError("Duplicate distance detected")
            dist_dict[dist] = [i, j]
    return dist_dict

# # Check all distances are unique
# for scanner in scanners:
#     compute_distances(scanner)

def compute_point_distances(scanner):
    dist_dict = {}
    for i, source in enumerate(scanner):
        for j, target in enumerate(scanner):
            if i == j:
                continue
            dist = compute_dist(source, target)
            current_dists = dist_dict.get(i, [])
            current_dists = sorted([*current_dists, dist])
            dist_dict[i] = current_dists
    return dist_dict

# Loop and find matches
point_list = []
match_list = []
for scan_nr, scanner in enumerate(scanners):
    dist_dict = compute_point_distances(scanner)
    for point_nr, dists in dist_dict.items():
        new_point = True
        for i, point in enumerate(point_list):
            overlap = set(point).intersection(dists)
            if len(overlap) > 3:
                new_point = False
                point_list[i] = sorted(list(set([*point, *dists])))
                match_list[i] = [*match_list[i], (scan_nr, point_nr)]
                new_point = False
                break
        if new_point:
            point_list.append(dists)
            match_list.append([(scan_nr, point_nr)])
# print(point_list)
print(len(point_list))

# Check for remaining dups
dups = 0
for i, s in enumerate(point_list):
    for j, t in enumerate(point_list):
        if i == j:
            break
        if len(set(s).intersection(t)) > 3:
            dups = dups + 1

print(len(point_list) - dups)


def rotation(s, sd, t, td):
    # print(s, sd, t, td)
    ds = s[0] - sd[0], s[1] - sd[1], s[2] - sd[2]
    dt = t[0] - td[0], t[1] - td[1], t[2] - td[2]
    transform = {}
    for si, se in enumerate(ds):
        for ti, te in enumerate(dt):
            if se == te:
                transform[si + 1] = ti + 1
            if se == te * -1:
                transform[si + 1] = (ti + 1) * -1
    return transform


def reverse_rotaion(scanner, transform):
    new_scanner = []
    for s in scanner:
        p = []
        for k, v in transform.items():
            p.append(s[abs(v)-1] * (abs(v)/v))
        new_scanner.append(p)
    return new_scanner


def get_scan_d(s, t):
    d = s[0] - t[0], s[1] - t[1], s[2] - t[2]


def find_point_set(s, t):
    sets = []
    for m in match_list:
        contained_scans = [e[0] for e in m]
        if (t in contained_scans) and (s in contained_scans):
            sp = None
            tp = None
            for e in m:
                if e[0] == s:
                    sp = e
                if e[0] == t:
                    tp = e
            sets.append(sp)
            sets.append(tp)
    if len(sets) >=4:
        print("found point set")
        return sets[0:4]
    else:
        return []

# find_point_set(0, 3)

rotated_scans = [0]
while len(rotated_scans) < len(scanners):
    print(rotated_scans)
    for scan_nr in range(len(scanners)):
        if scan_nr not in rotated_scans:
            print(scan_nr)
            for pot in rotated_scans:
                print(pot)
                point_set = find_point_set(pot, scan_nr)
                if len(point_set) == 4:
                    
                    # print(point_set)
                    
                    # rotate
                    transform = rotation(
                        scanners[point_set[0][0]][point_set[0][1]],
                        scanners[point_set[2][0]][point_set[2][1]],
                        scanners[point_set[1][0]][point_set[1][1]],
                        scanners[point_set[3][0]][point_set[3][1]],
                    )
                    
                    # reverse rotation
                    scanner = scanners[scan_nr]
                    scanner = reverse_rotaion(scanner, transform)
                    scanners[scan_nr] = scanner
                    
                    rotated_scans.append(scan_nr)
                    
                    break

has_distance = [0]
d_dict = {}



