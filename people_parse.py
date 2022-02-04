import numpy as np
import urllib.request, json, ssl, pickle
import matplotlib.pyplot as plt
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def requests_amt(person, fromd, tod, query=None):
    with urllib.request.urlopen(
            f'https://de.openparliament.tv/api/v1/search/media?q={query}&personID={person}&dateFrom={fromd}&dateTo={tod}',
            context=ctx) as url:
        data = json.loads(url.read().decode())
        return data["meta"]["results"]["total"]


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

print(len(filtered), len(pdic))
print(np.mean(anzs))
plt.hist(anzs, bins=15)
plt.savefig("peoplehist.png")

parties = {"FDP": "Q1387991",
           "CDU": "Q1023134",
           "Grüne": "Q1007353",
           "AFD": "Q42575708",
           "Linke": "Q1826856",
           "SPD": "Q2207512"}

print(filtered[0]["factionID"])
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
for word in words:
    anzs=[]
    for p in filtered:
        if "word_count" not in p:
            p["word_count"]=[]
        amt=requests_amt(p["id"],fromd,tod,word)
        p["word_count"].append(amt)
        anzs.append(amt)
    plt.hist(anzs, bins=15)
    plt.title(word)
    plt.savefig("people_"+word + ".png")
    plt.clf()

with open("person_words.pickle","wb") as f:
    pickle.dump(filtered,f)

