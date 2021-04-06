# Sorteando algo em uma lista (ARRAY)
import random
alunos = []
for c in range(0,3):
    aluno = input(f'Digite o nome do {c + 1}º aluno: ')
    alunos.append(aluno)

sorteado = random.choice(alunos)
print(alunos)
print(f'O aluno sorteado foi {sorteado}')
