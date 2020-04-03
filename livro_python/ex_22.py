"""Programa que faz cálculos núméricos"""

primeiro = int(input('Diga o primeiro número: '))
segundo = int(input('Diga o segundo número: '))
escolha = int(
    input('Escolha a operação: 1(soma),2(subtr),3(divis) e 4(multi): '))
calculo = 0
if escolha == 1:
    escolha = 'Soma'
    calculo = primeiro + segundo
elif escolha == 2:
    escolha = 'Subtração'
    calculo = primeiro - segundo
elif escolha == 3:
    escolha = 'Divisão'
    calculo = primeiro / segundo
elif escolha == 4:
    escolha = 'Multiplicação'
    calculo = primeiro * segundo

print(f'A {escolha} de {primeiro} e {segundo} é : {calculo:.2f}')
