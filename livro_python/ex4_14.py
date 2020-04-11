""" Programa que calcula poupança,
com depósito mensal."""

x = 0
poupanca = float(input('Diga o valor inicial R$: '))
deposito = float(input('Valor de depósito mensal R$: '))
juros = float(input('Valor de juros(%): '))
saldo = poupanca

while x <= 24:
    saldo = deposito + (saldo + (saldo * (juros / 100)))
    x = x + 1
    print(f'Mês {x}. Saldo de R${saldo:.2f}.')
print(f'Total acumulado é de R${saldo - poupanca:.2f}.')
