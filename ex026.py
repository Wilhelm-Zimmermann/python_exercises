# Analise pesada de string
import itertools
import threading
from time import sleep
import sys

frase = input('Digite uma frase: ').strip().upper()

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

print(f'\nA letra "A" aparece {frase.count("A")} vezes na frase')
print(f'A primeira letra "A" aparece na posição {frase.find("A") +1}')
print(f'A primeira letra "A" aparece na posição {frase.rfind("A") +1}')