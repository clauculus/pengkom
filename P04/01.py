# Problem 1

def jarak(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)

n = int(input('Masukkan jumlah kota: '))

x = [0 for i in range(n)]
y = [0 for i in range(n)]

for i in range (n):
    x[i] = int(input('Masukkan koordinat x kota ke ' + str(i+1) + ': '))
    y[i] = int(input('Masukkan koordinat y kota ke ' + str(i+1) + ': '))

total_jarak = 0

for i in range (n):
    if (i+1 <= n-1):
        total_jarak += jarak(x[i], y[i], x[i+1], y[i+1])

print('Jarak totalnya ' + str(total_jarak))
