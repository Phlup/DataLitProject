import numpy as np
words={}

with open("Koalitionsvertrag_2021-2025.txt", encoding="utf8") as f:
    text=f.read().split()
    for word in text:
        if len(word)<5:
            continue
        if word[0]==word[0].upper():
            if word not in words:
                words[word]=0
            words[word]+=1

mv=np.mean(list(words.values()))
arts=[]
for w in words:
    if words[w]>5:
        arts.append( (words[w],w))

arts.sort()
for x in arts:
    print(x)
print(mv)
