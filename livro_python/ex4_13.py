""" Programa que calcula poupança"""
x = 1
poupanca = float(input('Diga o valor inicial R$: '))
juros = float(input('Valor de juros: '))
saldo = poupanca
while x <= 24:
    saldo = saldo + (saldo * (juros / 100))
    x = x + 1
    print(f'Mês {x} o saldo é de R${saldo:.2f}.')
print(f'Total acumulado é de R${saldo - poupanca:.2f}.')
