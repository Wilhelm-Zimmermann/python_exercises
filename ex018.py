# Calculando,seno,cosseno, e tangente de um angulo
import math 

angulo = int(input('Digite o angulo: '))
radian = math.radians(angulo)
cos = math.cos(radian)
sen = math.sin(radian)
tan = math.tan(radian)

print(f'O ângulo digitado foi de {angulo}º graus')
print(f'O cosseno é de {cos:.2f}')
print(f'O seno é de {sen:.2f}')
print(f'O tangente é de {tan:.2f}')