def persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    print("luas persegi: ",luas)
    print("keliling: " ,keliling)

def persegi_panjang(panjang, lebar):  
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print("luas persegi panjang: ",luas)
    print("keliling persegi panjang: " ,keliling)
    
def lingkaran(jari):
    phi = 3.14
    luas = phi * jari * jari
    keliling = 2 * phi * jari
    print("luas lingkaran: ",luas)
    print("keliling lingkaran: " ,keliling)
    
def segitiga(alas,tinggi):
    luas = 0.5* alas * tinggi
    keliling = alas * 3
    print("luas segitiga: ",luas)
    print("keliling segitiga: " ,keliling)
    
def jajar_genjang(alas,tinggi, sisi_miring):
    luas = alas * tinggi
    keliling = 2* alas + sisi_miring
    print("luas jajar genjang: ",luas)
    print("keliling jajar genjang: " ,keliling)

def belah_ketupat(diagonal1,diagonal2,sisi):
    luas = 0.5 * diagonal1 * diagonal2
    keliling = 4 * sisi
    print("luas belah ketupat: ",luas)
    print("keliling belah ketupat: " ,keliling)
    
def layang_layang(d1,d2,sisi):
    luas = 0.5 * d1 * d2
    keliling = 4 * sisi
    print("luas layang layang: ",luas)
    print("keliling layang: " ,keliling)
    
      
                