import random
import numpy
comparison=0
def mergeSort(alist):
    global comparison
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            comparison=comparison+1
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    return comparison
def clear(num):
    global comparison
    comparison=0
for i in range(5,41,1):
    alist = numpy.random.permutation(i)
    output=mergeSort(alist.tolist())
    print("The output for n={:d} is {:d}".format(i,output))
    clear(output)
