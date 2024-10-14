from itertools import *
import itertools
alphabet = "РОСОМАХА"
s = dict(zip('РСМХ','0'*4))
s2 =dict(zip('ОА','1'*2))
s.update(s2)
print (s)
cnt=0
s3={x:alphabet.count(x) for x in s}
print (s3)
k=set()
for p in permutations(alphabet,5):
    d=""
    for x in p:
        d+=s[x]
    if '11' not in d and '00' not in d:
        if all((p.count(c)==s3[c] for c in p)):
            # print (p)
            cnt+=1
            k.add(p)
            print (p,cnt)


print (cnt,len(k))

