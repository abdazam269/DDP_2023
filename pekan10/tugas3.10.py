def duplikat (data):
    buah_duplikat = []
    for buah in data:
        buah_duplikat.append (buah)
        buah_duplikat.append (buah)
    return buah_duplikat

nama_buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
print(duplikat(nama_buah))
    
