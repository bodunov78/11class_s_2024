from itertools import *
import itertools

import itertools
k=0
glas='ИОА'
for p in itertools.permutations('МИТРОФАН',6):
    if sum([c in glas for c in p]) < 3 and sum([(p[i] in glas and p[i+1] in glas) for i in range(5)]) == 0:
        k+=1
print(k)