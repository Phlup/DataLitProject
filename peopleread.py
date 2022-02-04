import numpy as np
import urllib.request, json,ssl,pickle
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
def requests_amt(fromd,tod,person=None):
    if person==None:
        q=""
    else:
        q=f'personID={person}&'
    with urllib.request.urlopen(f'https://de.openparliament.tv/api/v1/search/media?{q}dateFrom={fromd}&dateTo={tod}',context=ctx) as url:
        data = json.loads(url.read().decode())
        return data["meta"]["results"]["total"]


with open("people.json", encoding="utf8") as f:
    dta=json.load(f)
parties={"FDP": "Q1387991",
"CDU": "Q1023134",
"Grüne": "Q1007353",
"AFD": "Q42575708",
"Linke": "Q1826856",
"SPD": "Q2207512"}

ps=set(parties.values())
want=[]
for p in dta:
    if p["factionID"] in ps:
        want.append(p)

fromd="2018-01-01"
tod="2022-01-01"

anzs=[]
for i  in range(len(want)):
    want[i]["anz"]=requests_amt(fromd,tod,want[i]["id"])
    anzs.append(want[i]["anz"])
    if anzs[-1]!=0:
        print(i,want[i]["anz"])

with open("people.pickle","wb") as f:
    pickle.dump(want,f)



print(np.mean(anzs))
