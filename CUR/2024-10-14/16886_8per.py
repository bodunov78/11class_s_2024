from itertools import *
cnt=0
for p in permutations('МАТВЕЙ'):
    s="".join(p)
    if s[0]!='Й' and 'АЕ' not in s:
        cnt+=1
print (cnt)