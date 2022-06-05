# Problem 3

N = int(input('Masukkan bilangan: '))
print('Pola yang terbentuk: ')

for i in range (N):
    for j in range (2*N):
        if (j <= N-1):
            if (j <= i):
                print(j % 10, end='')
            else:
                print(i % 10, end='')
        else:
            if (i <= 2*N - 1 - j):
                print(i % 10, end='')
            else:
                print((2*N - 1 - j) % 10, end='')

    print()

for i in range (N-1, -1, -1):
    for j in range (2*N):
        if (j <= N-1):
            if (j <= i):
                print(j % 10, end='')
            else:
                print(i % 10, end='')
        else:
            if (i <= 2*N - 1 - j):
                print(i % 10, end='')
            else:
                print((2*N - 1 - j) % 10, end='')

    print()
