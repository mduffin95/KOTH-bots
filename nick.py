# Parsing code
from sys import argv
import sys
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

if(n == 1):
    print("BDD")
    sys.exit(0)

result = []
for i in range(0,3):
    if(me["infected"] > 40 and me["healthy"] > me["migration"] * 5):
        result.append("Q")
        me["infected"] = me["infected"]-30
    elif(me["infected"] > 10):
        result.append("C")
        me["healthy"] = me["healthy"] + 10
        me["infected"] = me["infected"] - 10
    elif(me["contagion"] > 14):
        result.append("E")
        me["contagion"] = me["contagion"] - 8
    elif(me["infection"] > 10):
        result.append("M")
        me["infection"] = me["infection"] - 4
    elif(me["lethality"] > 10):
        result.append("I")
        me["lethality"] = me["lethality"] - 4
    elif(me["contagion"] > 5):
        result.append("V")
        me["contagion"] = me["contagion"] - 4
        me["lethality"] = me["lethality"] - 2
        me["infection"] = me["infection"] - 1
    else:
        result.append("D")
        me["infection"] = me["infection"] + 1
        me["contagion"] = me["contagion"] + 2

print(result[0] + result[1] + result[2])
