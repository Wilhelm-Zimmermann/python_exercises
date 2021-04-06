# calculando a area de uma parede
largura = float(input('Qual é a largura da sua parede? Em metros:'))
altura = float(input('Qual é a altura da sua parede? Em metros: '))
area = largura*altura
print(f'Sua parede tem a dimensao de {largura}x{altura} e sua area é de {area}m².')
print(f'Para pintar esta parede é necessario de {area * 0.5}l de tinta.')