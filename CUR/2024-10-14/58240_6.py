
from itertools import product
alphabet = '012345678'
ap=[]
for i in product(alphabet, repeat=5):
    if  i[0] != '0' and i[0] > i[1] > i[2] > i[3] > i[4]:
        ap.append(i)
print(len(ap))