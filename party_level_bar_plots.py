import pickle
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from tueplots import bundles


plt.rcParams.update(bundles.neurips2021())

with open("total_speaches_keywords.pickle","rb") as f:
    wordb=pickle.load(f)

with open("total_speaches.pickle","rb") as f:
    timedic=pickle.load(f)


colors = {"FDP":"yellow",
           "CDU":"black",
            "Grüne":"green",
            "AFD":"blue",
            "Linke":"purple",
           "SPD":"red"}


fig, (ax1, ax2) = plt.subplots(1, 2)
#fig.suptitle('Horizontally stacked subplots')
#ax1.plot(x, y)
#ax2.plot(x, -y)
x=np.array(range(0,len(wordb["Arbeit"]["CDU"])))
word="Arbeit"

for p in wordb[word]:
    ax1.plot(x,np.array(wordb[word][p])/(np.array(timedic[p])+1),label=p,linewidth=2.0,color=colors[p])

word="Bildung"
for p in wordb[word]:
    ax2.plot(x,np.array(wordb[word][p])/(np.array(timedic[p])+1),label=p,linewidth=2.0,color=colors[p])




plt.setp(ax1, xticks=[0,6,12,18,24,30,36,42,48] )
plt.setp(ax2, xticks=[0,6,12,18,24,30,36,42,48] )
#ax2.xticks([0,6,12,18,24,30,36,42,48])
ax1.legend()
ax1.set_xlabel("Month")
ax1.set_ylabel("Percentage of speeches")
ax1.set_title("Arbeit")
ax2.legend()
ax2.set_xlabel("Month")
ax2.set_ylabel("Speeches")
ax2.set_ylabel("Percentage of speeches")
ax2.set_title("Bildung")

plt.savefig("bar_arbeit_Bildung.pdf")



exit(0)

for word  in ["Arbeit","Bildung"]:
    fvalue, pvalue = stats.f_oneway(*list(wordb[word].values()))
    print(word,pvalue)
    for p in wordb[word]:
        x=np.array(range(0,len(wordb[word][p])))#+pi*wd
        plt.plot(x,np.array(wordb[word][p])/(np.array(timedic[p])+1),label=p,linewidth=2.0,color=colors[p])
    plt.xticks([0,6,12,18,24,30,36,42,48])
    plt.legend()
    plt.xlabel("Month")
    plt.ylabel("Percentage of speeches")
    plt.title(word)
    plt.savefig("bar_"+ word+".pdf")
    plt.clf()

summonth=np.array(timedic["CDU"]) + np.array(timedic["SPD"])  + np.array(timedic["Grüne"])  + np.array(timedic["FDP"])  + np.array(timedic["AFD"])
print(summonth[-10:])
for p in timedic:
    x=range(0,len(timedic[p]))
    plt.plot(x,timedic[p],label=p, alpha=1,color=colors[p])
plt.legend()

plt.xlabel("Month")
plt.ylabel("Speeches")
plt.title("Amount of speeches over time per party")
plt.xticks([0,6,12,18,24,30,36,42,48])
plt.savefig("parties_over_time.pdf")

plt.clf()
words=["Arbeit", "Digitalisierung", "Wirtschaft", "Forschung", "Bildung", "Kinder", "Frauen", "Vielfalt", "Klimaschutz", "Erneuerbare", "Bundeswehr", "Menschenrechte", "Nachhaltigkeit"]

for w in words:
    x=np.array(range(0,len(wordb[w]["CDU"])))
    y=np.array([0 for _ in x])
    nt=np.array([0.0001 for _ in x])
    for p in wordb[w]:
        if p in ["SPD","Grüne","FDP"]:
            continue
        y +=np.array(wordb[w][p])
        nt += np.array(timedic[p])
    print((np.round(100*sum(y)/sum(nt),4),w),",")
    #print(w,np.round(100*sum(y)/sum(nt),4),"%")
