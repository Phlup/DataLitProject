import pickle
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
with open("total_speaches_keywords.pickle","rb") as f:
    wordb=pickle.load(f)
    wordsums=[]
    for value in wordb:
        wordsums.append(wordb[value])

    categorysums=[]
    for value in wordb:
        for value2 in wordb[value]:
            categorysums.append(sum(wordb[value][value2]))

chunks = [categorysums[x:x+6] for x in range(0,len(categorysums),6)]


with open("total_speaches.pickle","rb") as f:
    timedic=pickle.load(f)
    sums=[]
    for value in timedic:
        sums.append(sum(timedic[value]))

norm_chunks=[]
for i in range (0,len(chunks)):
    norm_chunks.append(np.array(chunks[i])/np.array(sums))

exp_norm_chunks=[]
for i in range(len(norm_chunks)):
    exp_norm_chunks.append((sum(norm_chunks[i])/6))

exp_norm_chunks=[exp_norm_chunks[i:i+1] *6 for i in range(13)]



for i in range(len(norm_chunks)):
    print(stats.chisquare(f_obs=norm_chunks[i],f_exp=exp_norm_chunks[i]))


