# Calculando um reajuste salarial
salario = float(input('Qual o salario do funcionario? R$:'))
aumento = float(input('Qual o aumento a ser recebido? em porcentagem "%"'))
reajuste = (aumento / 100) * salario +salario

print(f'O funcionario com {aumento}% de aumento')
print(f'Agora recebe R${reajuste}')