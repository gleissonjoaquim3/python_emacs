"""Programa que faz uma tabuada com valores."""

n = int(input('Tabuada de : '))
inicio = int(input('De:'))  # Declaração do intervalo.
fim = int(input('Até:'))
x = inicio
while x <= fim:
    print(f'{n} x {x} = {n * x}')  # Mostra a multiplicaão dos valores.
    x = x + 1  # Contador de 1
