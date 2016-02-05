# Parsing code
from sys import argv
import numpy as np
# Healthy Infected Dead Infection Contagion Lethality Migration

args = argv[1].split(";")
n = int(args[0])
pid = int(args[1])
enemies = []
dead_states = 0
for p in args[2:]:
    res = [[int(p.split("_")[i]) for i in range(len(p.split("_")))]]
    if res[0][1] + res[0][2] > 0:
        if int(p.split("_")[0]) == pid:
            me = res[0]
        else:
            enemies += res
    else:
        dead_states += 1

enemies = np.array(enemies, np.int32) # all alive players
me = np.array(me, np.int32)
me = me[1:]
enemies = enemies[:,1:]
states = np.vstack((me, enemies))
# print(states)

def score(state):
    HEALTHY = 1
    INFECTED = 0.5
    DEAD = 0
    return state[0]*HEALTHY + state[1]*INFECTED + state[2]*DEAD

def apply_rules(state):
    if n % 5 == 0:
        state[0] += state[0] // 2
        state[1] += state[1] // 2

    # Infection
    state[0] -= state[3]
    state[1] += state[3]

    # Contagion
    conv = state[1] * (state[4] / 100)
    state[0] -= conv
    state[1] += conv
    if state[0] < 0:
        state[0] = 0

    # Extinction
    dead = state[1] * (state[5] / 100)
    state[1] -= dead
    state[2] += dead
    if state[1] < 0:
        state[1] = 0

    return(state)

def microbiology(state):
    state[3] -= 4
    if state[3] < 0:
        state[3] = 0
    return(state)

def epidemiology(state):
    state[4] -= 8
    if state[4] < 0:
        state[4] = 0
    return(state)

def immunology(state):
    state[5] -= 4
    if state[5] < 0:
        state[5] = 0
    return(state)

strategies = [microbiology, epidemiology, immunology]
strat_codes = ["M", "E", "I"]
code = ""
for i in range(3):
    print("The current iteration is", i)
    strat_scores = []
    scores_old = np.apply_along_axis(score, 1, states) # Find the scores for each state
    diff_old = scores_old[0] - scores_old[1:].mean() # Find difference between our score and the average of the enemies
    for j in range(len(strategies)):
        print("Strategy", j)
        res = states
        print(res)
        res[0,:] = strategies[j](res[0,:])
        print(res)
        res = np.apply_along_axis(apply_rules, 1, res) # Progress game on each state
        scores_new = np.apply_along_axis(score, 1, res) # Score each state
        diff_new = scores_new[0] - scores_new[1:].mean() # Find difference between our score and average of the enemies
        strat_scores += [diff_new - diff_old]
    # print("Scores", strat_scores)
    minimum = min(strat_scores)
    strat_scores = list(map(lambda x: x - minimum, strat_scores))
    tot = sum(strat_scores)
    if tot > 0:
        prob = list(map(lambda x: x / tot, strat_scores))
        # print(prob)
        res = np.random.choice(strat_codes, 1, p=prob)
        # print(prob, res)
    else:
        res = np.random.choice(strat_codes, 1)
    code += res[0]

print(code)
