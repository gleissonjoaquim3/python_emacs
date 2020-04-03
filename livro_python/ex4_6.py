""" Programa que faz cálculos númericos"""
p = int(input('Diga o primeiro número: '))
s = int(input('Diga o segundo número: '))
x = 1
r = 0
while x <= s:  # Repetirá até o valor de s
    r += p     # Faz a soma de p
    x += 1     # Contador
print(f'{p} x {s} = {r}')
