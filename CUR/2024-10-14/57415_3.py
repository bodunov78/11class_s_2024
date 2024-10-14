
from itertools import *
def fu1():
    s="АБЗИ"
    s=sorted(s)
    cnt=0
    for i in product(s,repeat=4):
        cnt+=1
        x="".join(i)
        if x=='ИЗБА':
            print (x,cnt)

def fu2():
    s="АБЗИ"
    s=sorted(s)
    cnt=0
    m=[0]
    for i in product(s,repeat=4):
        cnt+=1
        x="".join(i)
        m.append(x)

    print (m.index('ИЗБА'))
    # print (m)
fu2()