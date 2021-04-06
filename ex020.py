# Sorteando uma ordem na lista
import random
alunos = []
for c in range(0,4):
    aluno = input(f'{c+1}º aluno: ')
    alunos.append(aluno)
alunos.sort()
random.shuffle(alunos)
print('A ordem será: ')
for index,order in enumerate(alunos):
    print(f'{index + 1}º aluno: {order}')
