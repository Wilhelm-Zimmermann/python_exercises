# Calculando o preço do aluguel de um carro
dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos km ele andou? '))
totDias = dias * 60
totKm = km * 0.15
total = totDias + totKm

print(f'O aluguel ira custart R${total:.2f}')