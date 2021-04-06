# Calculando a hipotenusa
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = (ca * ca) + (co * co)
tot = hip ** (1/2)

print(f'A hipotenusa é {tot:.2f}')