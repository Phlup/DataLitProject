import numpy as np
import urllib.request, json,ssl,pickle
import matplotlib.pyplot as plt
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
def requests_amt(fromd,tod,person=None):
    '''
    gets the amount of speaches of a person in a specific timeframe
    :param fromd:
    :param tod:
    :param person:
    :return:
    '''
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
# filter to only the parties we want and unique
ps=set(parties.values())
want=[]
idsknown=set()
for p in dta:
    if p["factionID"] in ps and p["id"] not in idsknown:
        want.append(p)
        idsknown.add(p["id"])

fromd="2018-01-01"
tod="2022-01-01"

anzs=[]
# we get the amount of speeches per person and store the ones which have at least one
for i  in range(len(want)):
    want[i]["anz"]=requests_amt(fromd,tod,want[i]["id"])
    anzs.append(want[i]["anz"])
    if anzs[-1]!=0:
        print(i,want[i]["anz"])

with open("people_speaches.pickle","wb") as f:
    pickle.dump(want,f)


def requests_amt_p(person, fromd, tod, query=None):
    '''
    gets the amount of speeches of a person with a specific keyword
    :param person:
    :param fromd:
    :param tod:
    :param query:
    :return:
    '''
    with urllib.request.urlopen(
            f'https://de.openparliament.tv/api/v1/search/media?q={query}&personID={person}&dateFrom={fromd}&dateTo={tod}',
            context=ctx) as url:
        data = json.loads(url.read().decode())
        return data["meta"]["results"]["total"]


pdic=want
thresh = 50
fromd="2018-01-01"
tod="2022-01-01"
filtered = []
anzs = []
for p in pdic:
    if p["anz"] >= thresh:
        filtered.append(p)
        anzs.append(p["anz"])


#download the keywords for all the persons
words=["Arbeit", "Digitalisierung", "Wirtschaft", "Forschung", "Bildung", "Kinder", "Frauen", "Vielfalt", "Klimaschutz", "Erneuerbare", "Bundeswehr", "Menschenrechte", "Nachhaltigkeit"]
person_w_amt={}
for word in words:
    anzs=[]
    for p in filtered:
        if "word_count" not in p:
            p["word_count"]=[]
        amt=requests_amt_p(p["id"],fromd,tod,word)
        p["word_count"].append(amt)
        anzs.append(amt)


with open("persons_filtered_keywords.pickle","wb") as f:
    pickle.dump(filtered,f)
