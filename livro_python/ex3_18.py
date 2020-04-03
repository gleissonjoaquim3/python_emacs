""" Programa que lê 3 número e imprimi o maior e menor """

primeiro = int(input('Diga o primeiro número: '))
segundo = int(input('Diga o segundo número: '))
terceiro = int(input('Diga o terceiro número: '))

maior = primeiro

if segundo > primeiro:
    maior = segundo
if terceiro > segundo:
    maior = terceiro

menor = primeiro

if segundo < primeiro:
    menor = segundo
if terceiro < segundo:
    menor = terceiro
if terceiro:
    print('Teste')
