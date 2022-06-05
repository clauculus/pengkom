# Problem 2

clue = [' ', 'A', 'B', 'E', 'I', 'K', 'L', 'R', 'T', 'U']

n = int(input('Masukkan banyaknya bilangan: '))

bilangan = input('Masukkan bilangan: ')
string = ''

for bil in bilangan:
    string += clue[int(bil)]

print(string)


