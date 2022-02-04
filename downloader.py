
import urllib.request, json,ssl,pickle
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
def requests_amt(faction,fromd,tod,query=None):
    if query==None:
        q=""
    else:
        q=f'q={query}&'
    with urllib.request.urlopen(f'https://de.openparliament.tv/api/v1/search/media?{q}factionID={faction}&dateFrom={fromd}&dateTo={tod}',context=ctx) as url:
        data = json.loads(url.read().decode())
        return data["meta"]["results"]["total"]


months=[]
for year in range(2018,2022):
    for month in range(1,12):
        month=str(month)
        if len(month)==1:
            month= "0"+ month
        monthstr=f'{year}-{month}-01'
        months.append(monthstr)

parties={"FDP": "Q1387991",
"CDU": "Q1023134",
"Grüne": "Q1007353",
"AFD": "Q42575708",
"Linke": "Q1826856",
"SPD": "Q2207512"}

print(requests_amt("Q2207512","2021-01-01","2021-02-01"))
timedict={}
for party in parties:
    break
    print(party)
    timedict[party]=[]
    for m in range(len(months)-1):
        timedict[party].append(requests_amt(parties[party],months[m],months[m+1]))

with open("asdasd","wb") as f:
    pickle.dump(timedict,f)



wdic={}
for word in ["Arbeit", "Digitalisierung", "Wirtschaft", "Forschung", "Bildung", "Kinder", "Frauen", "Vielfalt", "Klimaschutz", "Erneuerbar", "Bundeswehr", "Menschenrechte", "Nachhaltigkeit"]:
    wdic[word]={}
    print(word)
    for party in parties:
        wdic[word][party]=[]
        for m in range(len(months)-1):
            wdic[word][party].append(requests_amt(parties[party],months[m],months[m+1],word))

with open("wordbla.pickle","wb") as f:
    pickle.dump(wdic,f)
