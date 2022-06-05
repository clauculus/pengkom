# Problem 1

N = int(input('Masukkan nilai N: '))
A = int(input('Masukkan nilai A: '))
B = int(input('Masukkan nilai B: '))
C = int(input('Masukkan nilai C: '))

for i in range (1, N+1):
    isMultiplier = False
    if (i % A == 0):
        print('Siap', end='')
        isMultiplier = True
    if (i % B == 0):
        print('Bang', end='')
        isMultiplier = True
    if (i % C == 0):
        print('Jago', end='')
        isMultiplier = True
    if not isMultiplier:
        print(i, end='')
    print(' ', end='')

