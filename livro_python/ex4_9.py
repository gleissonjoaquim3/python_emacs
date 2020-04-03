""" Uso dos acumuladore dentro do loop while"""
n = 1
soma = 0
while n <= 10:
    x = int(input(f'Digite o {n} número: '))
    soma += x
    n += 1
print(f'Soma: {soma}')
