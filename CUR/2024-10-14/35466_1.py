from itertools import *

s="ВЕРОНИКА"
s=sorted(set(s))
print (s)
cnt=0
for i in product(s,repeat=3):

    # print (i,cnt)
    if i.count('В')==1:
        cnt+=1
        if i.count('А')==0:
            print (i,cnt)