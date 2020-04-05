from kegiatanModul6 import *
from listMahasiswa import *

def convert(arr, obj):
    hasil=[]
    for x in range (len(arr)):
        for i in range (len(arr)):
            if arr[x] == obj[i].nim:
                hasil.append(obj[i])
    return hasil

def urutkanQuick():
    A = []
    for x in Daftar:
        A.append(x.nim)

    print("Quick Sort")
    quickSort(A)
    for x in convert(A, Daftar):
        print (x.nim)

def urutkanMerge():
    A = []
    for x in Daftar:
        A.append(x.nim)

    print("Merge Sort")
    mergeSort(A)
    for x in convert(A, Daftar):
        print (x.nim)

urutkanQuick()
urutkanMerge()
