import numpy as np
import urllib.request, json, ssl, pickle
import matplotlib.pyplot as plt
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


from tueplots import bundles


plt.rcParams.update(bundles.neurips2021())

with open("people_speaches.pickle", "rb") as f:
    pdic = pickle.load(f)
thresh = 50
fromd="2018-01-01"
tod="2022-01-01"
filtered = []
anzs = []
for p in pdic:
    if p["anz"] >= thresh:
        filtered.append(p)
        anzs.append(p["anz"])

parties={"FDP": "Q1387991",
"CDU": "Q1023134",
"Grüne": "Q1007353",
"AFD": "Q42575708",
"Linke": "Q1826856",
"SPD": "Q2207512"}
colors = {"Q1387991":"yellow",
           "Q1023134":"black",
            "Q1007353":"green",
            "Q42575708":"blue",
            "Q1826856":"purple",
           "Q2207512":"red"}


# plot a histogramm of the speakers
plt.hist(anzs, bins=15)
_, bins, _ = plt.hist(anzs, bins=50)
plt.clf()
cv=[]
cols=[]
lbls=[]
for party in parties:
    c=[]
    for p in pdic:
        if p["factionID"]==parties[party] and p["anz"] >=150:
            print(p["label"],p["anz"])
            c.append(p["anz"])
    cv.append(c)
    cols.append(colors[parties[party]])
    lbls.append(party)
cv=np.array(cv)
plt.hist(cv, 30, stacked=True, density = False,color=cols,label=lbls)
plt.legend()
plt.title("Stacked histogram of speeches given per person and party")
plt.xlabel("Speeches")
plt.ylabel("Persons")
plt.savefig("hist_speeches_people_parties.pdf")
plt.clf()

# check how many high frequency speackers each party has
ps = set(parties.values())

for pa in ps:
    nr = 0
    for p in filtered:
        if p["factionID"] == pa:
            nr += 1
    print(pa,colors[pa],nr)
plt.clf()
words=["Arbeit", "Digitalisierung", "Wirtschaft", "Forschung", "Bildung", "Kinder", "Frauen", "Vielfalt", "Klimaschutz", "Erneuerbare", "Bundeswehr", "Menschenrechte", "Nachhaltigkeit"]
person_w_amt={}

# create histograms for the high frequency speakers on the keywords
with open("persons_filtered_keywords.pickle", "rb") as f:
    filtered = pickle.load(f)
for word in words:
    i=0
    anzs=[]
    for p in filtered:
        anzs.append(p["word_count"][i])
    plt.hist(anzs, bins=15)
    plt.title(word)
    plt.savefig("people_"+word + ".pdf")
    plt.clf()
    i+=1



