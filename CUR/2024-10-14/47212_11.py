from itertools import *
import itertools
alphabet = "01234567"
s = dict(zip('0246','0006'))
s2 =dict(zip('1357','1111'))
s.update(s2)
print (s)
cnt=0
for x in range(8**4,8**5):
    # o=oct(x)[2:].zfill(5)
    o = oct(x)[2:]

    a=o
    # for i in a:
    #     o=o.replace(i,s[i])
    # print (a,o)
    a="".join((s[i] for i in o))
    if a.count('6')==1 and ('16' not in a and '61' not in a):

        cnt+=1
        print(a,o,cnt)
