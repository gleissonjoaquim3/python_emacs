""" Programa que resolve questões de provas"""
pontos = 0
questao = 1

while questao <= 3:
    resposta = input(f'Resposta da questão {questao}: ').upper()
    if questao == 1 and resposta == 'b' or resposta == 'B':
        pontos = pontos + 1
    if questao == 2 and resposta == 'c' or resposta == 'C':
        pontos = pontos + 1
    if questao == 3 and resposta == 'd' or resposta == 'D':
        pontos = pontos + 1
    questao = questao + 1
print(f'O aluno fez {pontos} ponto(s)')
