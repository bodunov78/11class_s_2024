from itertools import *
# !!!!
s="КОМПЬТЕР"
s=sorted(s)
cnt=0

for i in product(s,repeat=5):
    cnt+=1
    if i.count('К')==0 and i.count('Р')==2:
        print (i,cnt)