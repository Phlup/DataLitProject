import pickle
import matplotlib.pyplot as plt
import numpy as np
with open("wordbla.pickle","rb") as f:
    wordb=pickle.load(f)

with open("asdasd","rb") as f:
    timedic=pickle.load(f)

import scipy.stats as stats


for word  in wordb:
    fvalue, pvalue = stats.f_oneway(*list(wordb[word].values()))
    print(word,pvalue)
    for p in wordb[word]:
        x=range(0,len(wordb[word][p]))
        plt.plot(x,np.array(wordb[word][p])/(np.array(timedic[p])+1),label=p,linewidth=4.0)
    plt.legend()
    plt.title(word)
    plt.savefig(word+".png")
    plt.clf()
exit(0)

for p in timedict:
    x=range(0,len(timedict[p]))
    plt.plot(x,timedict[p],label=p)
plt.legend()
plt.savefig("asdas.png")
