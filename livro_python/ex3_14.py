# Programa de cálculo preço por kilometro
distan = int(input('Diga a distância perdorrida: '))
dias = int(input('Quantos dias foi usado o carro ? '))
cal_dias = (dias * 60)*(0.15 * distan)
print(f'Carro usado por {dias} dias e {distan}km rodados, custou um total de R${cal_dias:.2f}.')
