# Problem 2

bil_pertama = int(input('Masukkan bilangan pertama: '))
bil_kedua = int(input('Masukkan bilangan kedua: '))
bil_ketiga = int(input('Masukkan bilangan ketiga: '))
bil_keempat = int(input('Masukkan bilangan keempat: '))

# Cari bilangan minimum

min = 0
min1 = 0
min2 = 0

if (bil_pertama >= bil_kedua):
    min1 = bil_kedua
else:
    min1 = bil_pertama

if (bil_ketiga >= bil_keempat):
    min2 = bil_keempat
else:
    min2 = bil_ketiga

if (min1 >= min2):
    min = min2
else:
    min = min1

# Cari bilangan terbesar dari range 1..min yang habis membagi keempat bilangan
fpb = 1
for i in range (1, min+1):
    if (bil_pertama % i == 0 and bil_kedua % i == 0 and bil_ketiga % i == 0 and bil_keempat % i == 0):
        fpb = i

print('FPB dari keempat bilangan tersebut adalah', fpb)
