total = 0
# Mencakup angka ganjil dari 1 hingga 19
for i in range(1, 20, 2):  
    total += i

print(f"1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 = {total}")
# cara yg lain
bilangan = 1
jumlah =0

while bilangan <= 19:
    print (bilangan, end=" + ")
    jumlah += bilangan
    bilangan += 2

print("\b\b=",jumlah)