# Problem 3

def check_upper(x, y, N, M):
    return (N * x + M * y > N * M)

def check_lower(x, y, N, M):
    return (N * x + M * y < N * M)

def check_all_upper(b, k, N, M):
    return check_upper(k, b, N, M) and check_upper(k - 1, b, N, M) and check_upper(k - 1, b - 1, N, M) and check_upper(k, b - 1, N, M)

def check_all_lower(b, k, N, M):
    return check_lower(k, b, N, M) and check_lower(k - 1, b, N, M) and check_lower(k - 1, b - 1, N, M) and check_lower(k, b - 1, N, M)

def check_kotak(b, k, N, M):
    return check_all_upper(b, k, N, M) or check_all_lower(b, k, N, M)

N = int(input('Masukkan N: '))
M = int(input('Masukkan M: '))

for i in range (N, 0, -1):
    for j in range (1, M + 1):
        if check_kotak(i, j, N, M): # jika tidak dilewati diagonal
            print('0', end='')
        else:
            print('1', end='') # jika dilewati diagonal
    print()