# Problem 3

# Tuan Kin
x1 = float(input('Masukkan x1: '))
y1 = float(input('Masukkan y1: '))
# Tuan Ryo
x2 = float(input('Masukkan x2: '))
y2 = float(input('Masukkan y2: '))
# Restoran
x3 = float(input('Masukkan x3: '))
y3 = float(input('Masukkan y3: '))

# Jika ke Rumah Tuan Kin -> Tuan Ryo -> Restoran
distance_krr = abs(x1 - 0) + abs(y1 - 0) + abs(x2 - x1) + abs(y2 - y1) + abs(x3 - x2) + abs(y3 - y2)

# Jika ke Rumah Tuan Ryo -> Tuan Kin -> Restoran
distance_rkr = abs(x2 - 0) + abs(y2 - 0) + abs(x1 - x2) + abs(y1 - y2) + abs(x3 - x1) + abs(y3 - y1)

if (distance_krr >= distance_rkr):
    print('Jarak terpendeknya adalah ' + str(distance_rkr) +'.')
else:
    print('Jarak terpendeknya adalah ' + str(distance_krr) +'.')