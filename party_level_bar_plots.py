import pickle
import matplotlib.pyplot as plt
import numpy as np
with open("total_speaches_keywords.pickle","rb") as f:
    wordb=pickle.load(f)

with open("total_speaches.pickle","rb") as f:
    timedic=pickle.load(f)

import scipy.stats as stats
colors = {"FDP":"yellow",
           "CDU":"black",
            "Grüne":"green",
            "AFD":"blue",
            "Linke":"purple",
           "SPD":"red"}

for word  in wordb:
    fvalue, pvalue = stats.f_oneway(*list(wordb[word].values()))
    print(word,pvalue)
    for p in wordb[word]:
        x=range(0,len(wordb[word][p]))
        plt.bar(x,np.array(wordb[word][p])/(np.array(timedic[p])+1),label=p,linewidth=4.0, alpha=0.5,color=colors[p])
    plt.legend()
    plt.title(word)
    plt.savefig("bar_"+ word+".png")
    plt.clf()


for p in timedic:
    x=range(0,len(timedic[p]))
    plt.plot(x,timedic[p],label=p, alpha=1,color=colors[p])
plt.legend()
plt.savefig("parties_over_time.png")
