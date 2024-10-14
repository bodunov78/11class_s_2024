from itertools import *
from re import *
def fu1():
    s="АЛГОРИТМ"
    s=sorted(s)
    cnt=0
    for x in product(s,repeat=4):
        cnt+=1
        a="".join(x)
        # print (a,cnt)
        if match(r"^ИГ",a):
            print (a,cnt)

def fu2():
    s="АЛГОРИТМ"
    s=sorted(s)
    cnt=0
    for x in product(s,repeat=4):
        cnt+=1
        a="".join(x)
        # print (a,cnt)
        if a.startswith("ИГ",0):
            print (a,cnt)
fu2()