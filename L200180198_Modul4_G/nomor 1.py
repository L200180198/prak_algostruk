class Mhs(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

m0 = Mhs("Khumaila", 198, "Surakarta", 500000)
m1 = Mhs("Tery", 199, "Sukoharjo", 700000)
m2 = Mhs("Nevgy", 200, "Surakarta", 650000)
m3 = Mhs("Putri", 201, "Klaten", 55000)
m4 = Mhs("Rezki", 203, "Boyolali", 540000)
m5 = Mhs("Naufal", 204, "Magelang", 350000)
m6 = Mhs("Sultan", 205, "Klaten", 1000000)
m7 = Mhs("Elgar", 206, "Wonogiri", 545000)
m8 = Mhs("Devino", 207, "Klaten", 645000)
m9 = Mhs("Gina", 208, "Surakarta", 570000)
m10 = Mhs("Kevin", 209, "Purwodadi", 455000)

Daftar = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]

def cariKotaTinggal(list, target):
    a = []
    for i in list :
        if i.kotaTinggal == target:
            a.append(list.index(i))
    return a

a = cariKotaTinggal(Daftar, "Klaten")
print(a)
