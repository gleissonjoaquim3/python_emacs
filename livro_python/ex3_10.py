# Cálculo de aumento de salário
salario = float(input('Diga o valor do salário: '))
aumento = float(input('Quantos % de aumento ? '))
calc = salario + (salario / 100) * aumento
difer = calc - salario
print(f'Com um aumento de {aumento}%, seu salário R${salario:.2f} foi para R${calc:.2f}!\nR${difer:.2f} de aumento.')
