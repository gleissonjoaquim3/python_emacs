# Programa que calcula a velocidade média percorrida
veloc = int(input('Qual a velocidade média percorrida ?  '))
dist = int(input('Diga a distância percorrida(km): '))
tempo = dist / veloc
# Opcional: imprimir o tempo em horas, minutos e segundos
tempo_s = int(tempo * 3600)  # convertemos de horas para segundos
horas = int(tempo_s / 3600)  # parte inteira
tempo_s = int(tempo_s % 3600)  # o resto
minutos = int(tempo_s / 60)
segundos = int(tempo_s % 60)

print(f'Com uma velodicade média de {veloc}km/h.')
print(f'Com distância de {dist}km, gera um tempo total de {horas}h:{minutos}m:{segundos}s.')

