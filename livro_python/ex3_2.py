
# Programa 2.2 - Calculo de aumento de salário
# Composição de strings utilizando o f'string


sal = 750
aum = 15
por = sal + (sal * aum / 100)

print(f'O salário base de R${sal} com o aumento de {aum}% foi de: R${por}')

# Forma de Composição usando o .format

nome = 'Joao'
idade = 22
grana = 51.34

print('{} tem {} anos e R${} no bolso'.format(nome, idade, grana))

# Forma de Composição usanfo o fstring
nome = 'Joao'
idade = 22
grana = 51.34

print(f'{nome} tem {idade} anos e R${grana} no bolso')
