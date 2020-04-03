# Programa com o total de segundos

dias = int(input('Diga qts dias: '))
hrs = int(input('Diga qts horas: '))
minutos = int(input('Diga qts minutos: '))
segundos = int(input('Diga qts segundos: '))
sec = ((hrs * 3600) + (minutos * 60) + segundos) + (dias * 86400)
print(f'{dias} dia(s),{hrs} hr(s), {minutos} minuto(s), {segundos} segundos gera {sec} segundos !!')
