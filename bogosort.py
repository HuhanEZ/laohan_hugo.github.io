import random
import numpy
f=open("D:/result.txt",'w+')
def bogosort(lst):
    time=0
    while lst != sorted(lst):
        time=time+1
        print(lst)
        random.shuffle(lst)
    return time
for i in range(2,31,1):
    sort=numpy.random.permutation(i)
    comparsion=bogosort(sort.tolist())
    print("Total number of random shuffles used of n={:d} is {:d}".format(i,comparsion),file=f)
    print("Shuffles for n={:d} is {:d}".format(i,comparsion))