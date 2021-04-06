# Verifica se existe a palavra silva dentro da variavel
import itertools
import threading
from time import sleep
import sys

name = input('Digite seu nome completo: ').upper()

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rVerificando ' + c)
        sys.stdout.flush()
        sleep(0.1)
    sys.stdout.write('\rPronto!     ')

t = threading.Thread(target=animate)
t.start()

#long process here
sleep(4)
done = True

print(f'\nExiste Silva em nome {"SILVA" in name}')