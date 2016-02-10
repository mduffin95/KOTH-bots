from sys import argv

args = argv[1].split(";")
n = int(args[0])
pid = int(args[1])
dic = ["pid","healthy","infected","dead","infection","contagion","lethality","migration"]
players = []
for p in args[2:]:
    players += [{dic[i]:int(p.split("_")[i]) for i in range(len(p.split("_")))}]
    if int(p.split("_")[0]) == pid:
        me = players[-1]

code = ""
if(n < 50):
    while( len(code) < 3):
        if(me["migration"] > 0):
            code += "B" #
            me["migration"] -= 10
        if(me["lethality"] > 50):
            code += "I" # immunology
            me["lethality"] -= 4
        if(me["infected"] > me["healthy"]):
            code += "C"
            me["infected"] -= 10
            me["healthy"] += 10
        else:
            code += "T"
else:
    code = "CCC"

print(code)
