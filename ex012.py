# Calculando o desconto de um produto
produto = float(input('Quanto custa o produto? '))
desconto = float(input('Qual é a porcentagem do desconto? '))
n = desconto / 100
descontoTotal = produto * n
produtoDesconto = produto - descontoTotal

print(f'O produto com {desconto}% de desconto')
print(f'Custa agora R${produtoDesconto}')

print('')
print('Obrigado por usar nosso programa')