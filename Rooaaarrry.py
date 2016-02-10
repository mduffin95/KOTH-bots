from sys import argv
import random


args = argv[1].split(";")

# N: Do Nothing 
# M: Research Microbiology [Effects: Reduce local Infection Rate by 4] 
# E: Research Epidemiology [Effects: Reduce local Contagion Rate by 8%] 
# I: Research Immunology [Effects: Reduce local Lethality Rate by 4%] 
# V: Research Vaccination [Effects: Reduce local Infection Rate by one, reduce local Contagion Rate by 4%, reduce local Lethality Rate by 2%] 
# C: Give Cure [Effects: Convert 10 local Infected to Healthy] 
# Q: Quarantine [Effects: Remove 30 local Infected] 
# O: Open Borders [Effects: Increase local Migration Rate by 10%] 
# B: Close Borders [Effects: Decrease local Migration Rate by 10%] 
# T: BioTerrorism [Effects: Convert 4 global Healthy to Infected] 
# W: Weaponization [Effects: Increase global Infection Rate by 1, increase global Lethality Rate by 2%] 
# D: Dissemination [Effects: Increase global Infection Rate by 1, increase global Contagion Rate by 2%] 
# P: Pacification [Effects: Decrease global Infection Rate by 1, decrease global Contagion Rate by 1%, decrease global Lethality Rate by 1%] 

# Healthy: People not infected 
# Infected: People who can die from the pandemic 
# Dead: Body count, no particular effect (only scoring) 
# Infection Rate: Number of Healthy who will become Infected each turn 
# Contagion Rate: Percentage of Infected that will convert Healthy to Infected each turn 
# Lethality Rate: Percentage of Infected that will die each turn 
# Migration Rate: Percentage of both Healthy and Infected that will emigrate/immigrate each turn
# Local: Affects only your state 
# Global: Affects every state

n = int(args[0])
pid = int(args[1])
dic = ["pid","healthy","infected","dead","infection","contagion","lethality","migration"]
players = []
for p in args[2:]:
    players += [{dic[i]:int(p.split("_")[i]) for i in range(len(p.split("_")))}]
    if int(p.split("_")[0]) == pid:
        me = players[-1]

        if(me['healthy'] < 10):
          fo = open("will&testamentofRorySmith.txt", "wb")
          fo.write( "If you're reading this, Rory the Great has been vanquished...\nFear not, for he lives on in spirit and will haunt your dreams...");
          fo.close()

        if(me['healthy'] < me['infection']):
          #give up
          print("DCT")
          break
        else:
          # we're playing
          if(random.random() > 0.5):
            print("CQQ")
          else:
            print("CEQ")


