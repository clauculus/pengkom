# Problem 3

n = int(input('Masukkan panjang string: '))
string = input('Masukkan string: ')

max_length = 1

for i in range (n):
    for j in range (i + 1, n+1):
        substr = string[i:j]
        length_substr = j - i

        equal = True
        k = 0
        while (equal) and (k <= length_substr//2):
            if (substr[k] == substr[length_substr - 1 - k]):
                k += 1
            else:
                equal = False

        if (equal) and (length_substr > max_length):
            max_length = length_substr

print('Panjangnya adalah', max_length)