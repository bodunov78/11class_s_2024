from itertools import *
import itertools
alphabet = "ГЕРАСИМ"
s = dict(zip('ГРСМ','0'*4))
s2 =dict(zip('ЕАИ','1'*3))
s.update(s2)
print (s)
cnt=0
for p in permutations("ГЕРАСИМ"):
    d=""
    for x in p:
        d+=s[x]
    if '11' not in d and '00' not in d:
        cnt+=1

print (cnt)

