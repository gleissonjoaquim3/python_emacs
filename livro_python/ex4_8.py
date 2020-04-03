""" Mais exemplos de contadores sendo usados 
dentro de condições"""

pontos = 0
questao = 1
while questao <= 3:
    resposta = input(f'Resposta da questão {questao}: ')
    if questao == 1 and (resposta == 'b' or resposta == 'B'):
        pontos += 1  # Faz a função de contador.
    if questao == 2 and (resposta == 'a' or resposta == 'A'):
        pontos += 1
    if questao == 3 and (resposta == 'd' or resposta == 'D'):
        pontos += 1
    questao += 1     # Faz a função de contador.
print(f'O aluno fez {pontos} ponto(s).')
