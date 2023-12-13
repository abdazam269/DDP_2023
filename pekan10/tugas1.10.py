
def lulus_aja(data):
    lulus = []
    for mhs in data:
        if mhs['nilai'] > 60:
            lulus.append(mhs['nama'])
    return lulus

hasil_akhir = [
{'nama':'bagas', 'nilai':76},
{'nama':'andri', 'nilai':70},
{'nama':'bambang', 'nilai':90},
{'nama':'nizar', 'nilai':20}
]

print(lulus_aja(hasil_akhir))