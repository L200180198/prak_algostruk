from kegiatanModul5 import *

class MhsTIF(object):
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', nim ' + str(self.nim)\
            + '. Tinggal di ' + self.kota\
            + '. Uang saku Rp ' + str(self.uangSalu)\
            + '. tiap bulannya.'
        return s

k0 = MhsTIF("Keisya", 20, "Surakarta", 240000)
k1 = MhsTIF("Nevgy", 31, "Sragen", 230000)
k2 = MhsTIF("Purwanto", 2, "Surakarta", 250000)
k3 = MhsTIF("Calisa", 28, "Surakarta", 235000)
k4 = MhsTIF("Nada", 4, "Boyolali", 240000)
k5 = MhsTIF("Lintang", 41, "Salatiga", 250000)
k6 = MhsTIF("Denis", 13, "Klaten", 245000)
k7 = MhsTIF("Kevin", 15, "Wonogiri", 245000)
k8 = MhsTIF("Alfin", 23, "Klaten", 245000)
k9 = MhsTIF("Khumaila", 64, "Sukoharjo", 270000)
k10 = MhsTIF("Kholid", 59, "Boyolali", 265000)

Daftar = [k0, k1, k2, k3, k4, k5, k6, k7, k8, k9, k10]

def urutkanNim(list):
    NIM = []
    for i in list:
        NIM.append(i.nim)
    insertionSort(NIM)
    return NIM
