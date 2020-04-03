"""Programa que faz cálculos númericos"""
p = int(input('Informe o primeiro divisor: '))
s = int(input('Informe o segundo dividendo: '))
x = p
q = 0
while x >= s:
    q += 1
    x -= s
resto = x
print(f'{p} / {s} = {q}')
