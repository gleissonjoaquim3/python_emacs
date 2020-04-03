""" Programa que faz aprovação bancaria"""

casa = int(input('Diga o valor da casa: '))
salario = float(input('Informe o valor do seu salário: '))
parcela = int(input('Informe a quantidade de parcelas: '))

porcentagem = salario - (salario / 100) * 70
valor_presta = casa / parcela

if valor_presta < porcentagem:
    print(f'Sua parcela de R${valor_presta:.2f} está aprovada !')
else:
    print('Infelizmente não será possível financiar.')
