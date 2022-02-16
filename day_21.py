"""Day 21 entry"""

# Settings
path_data = "day_21.txt"

# Test Data
input = open(path_data).readlines()
input = [e.strip() for e in input]
print(input)


def roll():
    """Roll generator"""
    ii = 0
    while True:
        ii = ii + 1
        if ii > 100:
            ii = 1
        yield ii


r = roll()

p_positions = [int(e.split(" ")[-1]) for e in input]
# p_positions = [4, 8]
p_scores = [0] * len(p_positions)
turn_count = 0
while max(p_scores) < 1000:
    for p_nr in range(len(p_scores)):
        turn_score = 0
        for roll_nr in range(3):
            turn_score = turn_score + next(r)
            turn_count = turn_count + 1
        p_positions[p_nr] = (p_positions[p_nr] + turn_score - 1) % 10 + 1
        p_scores[p_nr] = p_scores[p_nr] + p_positions[p_nr]
        if max(p_scores) >= 1000:
            break
print(min(p_scores) * turn_count)


# --- PART 2 ---

# Use dict of dict to track how many games are in that state

# Game states (finite)
21 * 21 * 10 * 10 * 2

# Get roll count options (also finite)
vals = []
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            vals.append(i + j + k)
roll_val_counts = {e: vals.count(e) for e in set(vals)}
print(roll_val_counts)


# Hashable struct to track state
class State(object):

    def __init__(self, positions, scores, nr):
        self.positions = positions
        self.scores = scores
        self.nr = nr

    def __hash__(self):
        hash = 0
        hash = hash * 100 + self.positions[0]
        hash = hash * 100 + self.positions[1]
        hash = hash * 100 + self.scores[0]
        hash = hash * 100 + self.scores[1]
        hash = hash * 100 + self.nr
        return hash

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __str__(self):
        return " - ".join([
            " ".join([str(e) for e in self.positions]),
            " ".join([str(e) for e in self.scores]),
            str(self.nr)
        ])

    def __repr__(self):
        return self.__str__()


# Initialize starting position
p_wins = [0, 0]
p_positions = [int(e.split(" ")[-1]) for e in input]
# p_positions = [4, 8]
p_scores = [0] * len(p_positions)
p_nr = 0

# Initialize state dict
s = State(p_positions, p_scores, p_nr)
state_dict = {s: 1}

# s.__hash__()

win_score = 21
max_it = 1

it_count = 0
while len(state_dict) > 0:
    new_state_dict = {}
    for s, count in state_dict.items():
        # print("pre: ", s)
        for roll_val, roll_count in roll_val_counts.items():

            # Get new state
            new_positions = s.positions.copy()
            new_positions[s.nr] = (new_positions[s.nr] + roll_val - 1) % 10 + 1
            new_scores = s.scores.copy()
            new_scores[s.nr] = new_scores[s.nr] + new_positions[s.nr]
            new_nr = 1 if s.nr == 0 else 0
            new_state = State(new_positions, new_scores, new_nr)
            # print(roll_val, " - ", new_state)

            # Check for wins
            if max(new_scores) >= win_score:
                p_wins[s.nr] = p_wins[s.nr] + (roll_count * count)
            else:
                new_state_dict[new_state] = new_state_dict.get(new_state, 0) + (roll_count * count)
    state_dict = new_state_dict
    it_count = it_count + 1
    print(len(state_dict))   
    # print(max(p_wins))
    # if it_count >= max_it: 
    #     break   
print(p_wins)   
print(max(p_wins))   
print(444356092776315)
print(341960390180808)   

state_dict.items()
sum(state_dict.values())

27 * 27
