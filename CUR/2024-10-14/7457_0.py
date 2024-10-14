from itertools import *
def fu1():
    s=list("КЛРТ")
    s.sort()
    cnt=0
    print (s)
    for c1 in s:
        for c2 in s:
            for c3 in s:
                for c4 in s:
                    c=c1+c2+c3+c4
                    cnt+=1
                    if cnt==67:
                        print (c,cnt)

def fu2():

    s=sorted("КЛРТ")
    # print (s)
    m=[0]+list(product(s,repeat=4))
    print (m[67])
    # print (m)

def fu3():

    s=sorted("КЛРТ")
    # print (s)
    m=dict()

    for i in product(s,repeat=4):

        m[len(m)+1]=i
    print (m[67])
    print (m)


def fu4():
    s = sorted("КЛРТ")
    # print (s)
    m = dict()

    m={ (len(m) + 1):i  for i in product(s, repeat=4)}
        # m[len(m) + 1] = i
    # print(m[67])
    print(m)


fu4()