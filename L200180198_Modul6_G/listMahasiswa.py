class MhsTIF(object):
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', nim ' + str(self.nim)\
            + '. Tinggal di ' + self.kota\
            + '. Uang saku Rp ' + str(self.uangSaku)\
            + '. tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.nim
    def ambilUangSaku(self):
        return self.uangSaku

c0 = MhsTIF("Khumaila", 30, "Menco", 240000)
c1 = MhsTIF("Nam JooHyuk", 31, "Rajawali", 230000)
c2 = MhsTIF("Park SeooJoon", 29, "Mendungan", 250000)
c3 = MhsTIF("Ji ChangWook", 10, "Slamet Riyadhi", 235000)
c4 = MhsTIF("Joo JiHoon", 4, "Ahmad Yani", 240000)
c5 = MhsTIF("Lee DongWook", 61, "Blulukan", 250000)
c6 = MhsTIF("Kim Yohan", 19, "Gatak", 245000)
c7 = MhsTIF("Kang Haneul", 5, "Garuda Mas", 245000)
c8 = MhsTIF("Jang Dong Yoon", 23, "Elang Mas", 245000)
c9 = MhsTIF("Park HyungShik", 54, "Menco", 270000)
c10 = MhsTIF("Choi WooShik", 59, "Makam Haji", 265000)

c0.next = c1
c1.next = c2
c2.next = c3
c3.next = c4
c4.next = c5
c5.next = c6
c6.next = c7
c7.next = c8
c8.next = c9
c9.next = c10

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
