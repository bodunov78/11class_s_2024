from itertools import *
from re import *
def fu1():
    s="МАНГУСТ"
    s=sorted(s)
    cnt=0
    for x in product(s,repeat=6):
        cnt+=1
        a="".join(x)
        # print (a,cnt)
        if a[0]!="У" and a.count('М')==2 and a.count('Г')<=1:
            print (a,cnt)

fu1()