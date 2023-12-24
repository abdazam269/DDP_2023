class Binatang:
    def __init__(self, nama, makanan, habitat, berkembangbiak):
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
        self.berkembangbiak = berkembangbiak

    def info(self):
        print("nama\t:", self.nama)
        print("makanan\t:", self.makanan)
        print("habitat\t:", self.habitat)
        print("berkembangbiak\t:", self.berkembangbiak)
 
class Ular(Binatang):
    def __init__(self, nama, habitat):
        super().__init__(nama, "daging", habitat, "bertelur")

    def melilit(self):
        print(self.nama, "melilit mangsa")
        print("======================")


class Ayam(Binatang):
    def __init__(self, nama, habitat):
        super().__init__(nama, "selaganya", habitat, "bertelur")

    def matuk(self):
        print(self.nama, "matuk")
        print("======================")


class Elang(Binatang):
    def __init__(self, nama, habitat):
        super().__init__(nama, "ular", habitat, "bertelur")

    def terbang(self):
        print(self.nama, "terbang cepat")
        print("======================")


# Pemanggilan
singa = Ular("Ular", "tempat lembab")
singa.info()
singa.melilit()

ayam = Ayam("ayam", "kandang ayam")
ayam.info()
ayam.matuk()

elang = Elang("elang pitak", "puncak")
elang.info()
elang.terbang()