# Daftar harga
menu_makanan = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 12000,
    "Ayam Geprek": 18000
}

# Daftar menu 
menu_minuman = {
    "Aneka Jus": 15000,
    "Soft Drink": 10000,
    "Sweet Ice Tea": 5000
}

# input
nama_pembeli = input("Masukkan Nama Pembeli: ")
no_hp_pembeli = input("Masukkan No Hp Pembeli: ")
jenis_pesanan = input("Pesan Menu Apa? (makanan atau minuman): ")

if jenis_pesanan.lower() == "makanan":
    print("Daftar Menu Makanan:")
    for menu, harga in menu_makanan.items():
        print(f"{menu}: Rp. {harga}")

    pesanan = input("Masukkan pesanan: ")
    jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))

    if pesanan in menu_makanan:
        harga_total = menu_makanan[pesanan] * jumlah_pesanan
    else:
        print("Menu tidak valid.")
        exit()

elif jenis_pesanan.lower() == "minuman":
    print("daftar menu minuman:")
    for menu, harga in menu_minuman.items():
        print(f"{menu}: Rp. {harga}")

    pesanan = input("masukkan pesanan: ")
    jumlah_pesanan = int(input("masukkan jumlah pesanan: "))

    if pesanan in menu_minuman:
        harga_total = menu_minuman[pesanan] * jumlah_pesanan
    else:
        print("Menu tidak ada.")
        exit()
else:
    print("Jenis pesanan tidak ada.")
    exit()

# Output
print("Nama Pembeli:", nama_pembeli)
print("No Hp Pembeli:", no_hp_pembeli)
print("Menu yang di Pesan:", pesanan)
print("Jumlah pesanan:", jumlah_pesanan)
print("Harga yang harus dibayarkan: Rp", harga_total)
