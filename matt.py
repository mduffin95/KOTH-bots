# Parsing code
from sys import argv
from numpy.random import choice

args = argv[1].split(";")
n = int(args[0])
pid = int(args[1])
dic = ["pid","healthy","infected","dead","infection","contagion","lethality","migration"]
players = []
for p in args[2:]:
    players += [{dic[i]:int(p.split("_")[i]) for i in range(len(p.split("_")))}]
    if int(p.split("_")[0]) == pid:
        me = players[-1]

# Find all that are still alive and take their values.
# Calculate moving average of these values.
# Perhaps look at those above in the ranking and target them?
# Re-calculate probabilities after each choice.

def apply_rules(stats):
    if n % 5 == 0:
        stats = reproduce(stats)
    # Phase 4 - Infection
    stats["healthy"] -= stats["infection"]
    stats["infected"] += stats["infection"]
    if stats["healthy"] < 0:
        stats["healthy"] = 0
    # Phase 5 - Contagion
    conv = stats["infected"] * (stats["contagion"] / 100)
    stats["healthy"] -= conv
    stats["infected"] += conv
    if stats["healthy"] < 0:
        stats["healthy"] = 0
    # Phase 6 - Extinction
    dead = stats["infected"] * (stats["lethality"] / 100)
    # print(stats["infected"], stats["lethality"], dead)
    stats["infected"] -= dead
    if stats["infected"] < 0:
        stats["infected"] = 0
    # print stats
    return stats

def score(stats):
    # print("Scoring", stats["healthy"], stats["infected"])
    return -2*stats["healthy"] + 1.5*stats["infected"]

def reproduce(stats):
    stats["healthy"] += stats["healthy"] // 2
    stats["infected"] += stats["infected"] // 2
    return stats

def microbiology(stats):
    stats["infection"] -= 4
    if stats["infection"] < 0:
        stats["infection"] = 0
    stats = apply_rules(stats)
    # print(stats)
    return score(stats)

def epidemiology(stats):
    stats["contagion"] -= 8
    if stats["contagion"] < 0:
        stats["contagion"] = 0
    stats = apply_rules(stats)
    return score(stats)

def immunology(stats):
    stats["lethality"] -= 4
    if stats["lethality"] < 0:
        stats["lethality"] = 0
    stats = apply_rules(stats)
    return score(stats)

before = score(me)
# print("Before =", before)
a = microbiology(me) - before
b = epidemiology(me) - before
c = immunology(me) - before
scores = [a, b, c]
minimum = min(scores)
scores = list(map(lambda x: x - minimum, scores))
tot = sum(scores)
arr = ["M", "E", "I"]
if tot > 0:
    prob = list(map(lambda x: x / tot, scores))
    res = choice(arr, 3, p=prob)
    # print(prob, res)
else:
    res = choice(arr, 3)

code = ''.join(res)
print(code)

# Store historic levels
# Create moving average
# Use moving average to decide strategy
#
