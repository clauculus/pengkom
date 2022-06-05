# Problem 1

M = int(input('Masukkan M: '))

daftar_plat = [0 for i in range (M)]

for i in range (M):
    daftar_plat[i] = int(input('Masukkan pelat nomor mobil ke-' + str(i+1) + ': '))

N = int(input('Masukkan N: '))

for i in range (N):
    count = 0
    for plat in daftar_plat:
        if (plat % N == i):
            count += 1

    print('Anak ke-' + str(i+1) + ' mendapatkan ' + str(count) + ' mobil')

