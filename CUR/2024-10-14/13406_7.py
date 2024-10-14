
import itertools
alphabet = "ABCD"
s = 'XYZ'
ar = itertools.product(s,alphabet,alphabet,alphabet )
arl = []
count=0
for i in ar:
    arl.append(list(i))
    count += 1
print(count)