import numpy as np
import urllib.request, json, ssl, pickle
import matplotlib.pyplot as plt
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE




with open("people.pickle", "rb") as f:
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


print(len(filtered), len(pdic))
print(np.mean(anzs))
plt.hist(anzs, bins=15)
_, bins, _ = plt.hist(anzs, bins=50)
plt.clf()
for party in parties:
    c=[]
    for p in pdic:
        if p["factionID"]==parties[party]:
            c.append(p["anz"])
    plt.hist(c, bins=bins, alpha=0.3,color=colors[parties[party]])

plt.savefig("hist_speeches_people_parties.png")
plt.clf()


ps = set(parties.values())
for pa in ps:
    print(pa)
    nr = 0
    for p in filtered:
        if p["factionID"] == pa:
            nr += 1
    print(nr)
plt.clf()
words=["Arbeit", "Digitalisierung", "Wirtschaft", "Forschung", "Bildung", "Kinder", "Frauen", "Vielfalt", "Klimaschutz", "Erneuerbare", "Bundeswehr", "Menschenrechte", "Nachhaltigkeit"]
person_w_amt={}


with open("persons_filtered_keywords.pickle", "rb") as f:
    filtered = pickle.load(f)
for word in words:
    i=0
    anzs=[]
    for p in filtered:
        anzs.append(p["word_count"][i])
    plt.hist(anzs, bins=15)
    plt.title(word)
    plt.savefig("people_"+word + ".png")
    plt.clf()
    i+=1



