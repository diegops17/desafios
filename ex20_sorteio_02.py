import random
aluno1 = str(input('Informe o primeiro aluno: '))
aluno2 = str(input('Informe o segundo aluno: '))
aluno3 = str(input('Informe o terceiro aluno: '))
aluno4 = str(input('Informe o quarto aluno: '))

lista_alunos = aluno1, aluno2, aluno3, aluno4

aluno_sorteado = random.sample(lista_alunos, k=4)

print(f'Aluno sorteado: {aluno_sorteado}')