nilai = int(input("masukan nilai: "))
def kelulusan(nilai):
    if nilai <= 60:
        return "gagal"
    elif nilai <= 70:
        return "baik"
    elif nilai <= 80:
        return "sangat baik"
    elif nilai <= 100:
        return "sempurna"
    else:
        return "Nilai tidak valid"
print(kelulusan(nilai))