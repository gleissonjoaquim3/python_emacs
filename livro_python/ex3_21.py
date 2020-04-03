""" Programa que calcula distancia percorrida"""
distancia = int(input('Diga qual distância percorrica em km: '))
viagem1 = distancia * .50
viagem2 = distancia * .45
cobranca = 0

if distancia < 200:
    cobranca = viagem1
else:
    cobranca = viagem2
print(f'Sua viagem de {distancia}km, deu um total de R${cobranca}.')
