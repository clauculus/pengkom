# Problem 2

# Menerima koefisien a dan b
a = float(input('Masukkan a: '))
b = float(input('Masukkan b: '))


if (a != 0 and b != 0): # Jika a != 0 dan b != 0
    print('Integral dari f(x) adalah ' + str(int(a/2)) + 'x^2+' + str(b) + 'x+C')
elif (a == 0 and b == 0): # Jika a == 0 dan b == 0
    print('C')
elif (a == 0 and b != 0): # Jika a == 0 dan b != 0
    print('Integral dari f(x) adalah ' + str(b) + 'x+C')
else: # Jika a != 0 dan b == 0
    print('Integral dari f(x) adalah ' + str(a/2) + '+C')

