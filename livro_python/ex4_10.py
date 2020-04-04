""" Programa que faz loops em repetições"""
x = 1
while x <= 10:
    print(x)
    x += 1
    if x == 7:
        print('Igual a 6 !')
        break
print('Fim do loop while.')
