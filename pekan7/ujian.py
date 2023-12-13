# input
nama_kendaraan = input("Nama kendaraan? (contoh: mobil, motor): ")
jenis_bensin = input("Jenis bensin? (pertalite, pertamax, pertamax turbo): ")
kota_tujuan = input("Kota yang dituju? (jakarta, bekasi, depok, tangerang, bogor): ")

# data bensin dan jarak
jarak_kota = {
    "jakarta": 20,
    "bekasi": 35.7,
    "depok": 5,
    "tangerang": 99,
    "bogor": 120.6
}

bensin = {
    "pertalite": {"harga": 10000, "jarak_tempuh": 12},
    "pertamax": {"harga": 14000, "jarak_tempuh": 13},
    "pertamax turbo": {"harga": 17000, "jarak_tempuh": 13.5}
}

# Menghitung pemakaian bensin
jarak = jarak_kota.get(kota_tujuan, 0)
jarak_tempuh = bensin[jenis_bensin]["jarak_tempuh"]
pemakaian_bensin = jarak / jarak_tempuh

# Menghitung total harga
harga_per_liter = bensin[jenis_bensin]["harga"]
total_harga = pemakaian_bensin * harga_per_liter

# Menampilkan output
print("\nOutput:")
print("Nama Kendaraan:", nama_kendaraan)
print("Jenis Bensin:", jenis_bensin)
print("Kota yang Dituju:", kota_tujuan)
print("Pemakaian Bensin:", pemakaian_bensin,"liter" )
print("Total Harga dari Bensin:", total_harga,"rupiah" )