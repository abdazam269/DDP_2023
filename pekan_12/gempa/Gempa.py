
class Gempa:
    
    def __init__(self,lokasi,skala):
        self.lokasi = lokasi
        self.skala = skala
    
    def dampak(self,):
        if self.skala < 2 :
            print(f"dampak gempa {self.lokasi} tidak berasa")
        elif 2<= self.skala < 4 :
            print(f"dampak gempa {self.lokasi} bangunan retak-retak")
        elif 4 <= self.skala <6 :
            print(f"dampak gempa {self.lokasi} bangunan roboh")
        else:
            print(f"dampak gempa {self.lokasi} bangunan roboh dan berpotensi tsunami")
    
kota1 = Gempa("banten",1.2)
kota2 = Gempa("palu",6.1)
kota3 = Gempa("cianjur",5.6)
kota4 = Gempa("jayapura",3.3)
kota5 = Gempa("garut",4.0)


