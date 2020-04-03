# Programa que faz desconto

produto = float(input('Diga o valor do produto: '))
descon = float(input('Diga o % do desconto: '))
cal_desconto = produto - (produto / 100) * descon
dif_prod = produto - cal_desconto

print(f'Valor original de R$ {produto}, com {descon}% de desconto.')
print(f'Sai por R${cal_desconto:.2f}, com uma redução de R${dif_prod:.2f}.')
