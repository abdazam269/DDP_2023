def cari_ganjil(*angka):
    for i in angka:
        if i % 2==1:
            print("angka ganjil ditemukan: ", i)
            # return = hanya memanggil angka ganjil pertama
                   
cari_ganjil(2, 446, 884, 974, 276, 798, 123, 776, 13, 871)