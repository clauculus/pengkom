# Problem 2

def is_bomb(i, j, matriks):
    return matriks[i][j] == '*'

def count_side(i, j, b, k, matriks):
    count = 0
    if (j - 1 >= 0):
        if is_bomb(i, j - 1, matriks):
            count += 1
    if (j + 1 <= k - 1):
        if is_bomb(i, j + 1, matriks):
            count += 1
    if is_bomb(i, j, matriks):
        count += 1
    return count

def count_bombs(i, j, b, k, matriks):
    count = 0
    if (i - 1 >= 0):
        count += count_side(i - 1, j, b, k, matriks)
    if (i + 1 <= b - 1):
        count += count_side(i + 1, j, b, k, matriks)
    count += count_side(i, j, b, k, matriks)

    return count

def print_matriks(b, k, matriks):
    for i in range (b):
        for j in range(k):
            if is_bomb(i, j, matriks):
                print('#', end='')
            else:
                print(count_bombs(i, j, b, k, matriks), end='')
        print()

b = int(input('Masukkan jumlah baris matriks: '))
k = int(input('Masukkan jumlah kolom matriks: '))

print('Masukkan matriks:')

matriks = [['-' for i in range (k)] for i in range (b)]

for i in range (b):
    for j in range(k):
        matriks[i][j] = input('Masukkan elemen baris ' + str(i+1) + ' kolom ' + str(j+1) + ': ')
    
print_matriks(b, k, matriks)


