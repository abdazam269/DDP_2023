class orang :
    def __init__(self, fnama, lanma):
        self.fnama = fnama
        self.lnama = lanma
        
    def makan (self):
        print("saya bisa makan")
        
    def cetak(self):
        print("nama saya", self.fnama, self.lnama)
        
class Mahasiswa(orang):
    def __init__(self, fnama, lanma, prodi, angkatan):
        super().__init__(fnama, lanma)
        self.prodi = prodi
        self.angkatan = angkatan
        
    def cetak(self):
        super().cetak()
        print("saya prodi",self.prodi,"angkatan", self.angkatan)
    
class pegawai(orang):
    def bekerja(self):
        print("saya bekerja")
        
# #objek orang
# x = orang ("Bagus", "Maulana")
# x.cetak()

#objek mahasiswa
y = Mahasiswa ("farhan", "kebab", "Teknik informatika", 2023)
y.cetak()
y.makan

#objek pegawai
agus = pegawai("agus", "kepin")
agus.bekerja()