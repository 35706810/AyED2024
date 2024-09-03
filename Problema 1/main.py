import random
import time
from burbuja import burbuja
from quicksort import quicksort
from radix_sort import radix_sort

def medir_tiempos():
    tamaños = [100, 500, 1000, 10000, 100000, 1000000]
    for tamaño in tamaños:
        lista = [random.randint(0, 99999) for _ in range(tamaño)]

        # Medir tiempo de burbuja
        if tamaño <= 1000: 
            start = time.time()
            burbuja(lista.copy())
            end = time.time()
            print(f'Burbuja con tamaño {tamaño}: {end - start:.6f} segundos')

        # Medir tiempo de quicksort
        start = time.time()
        quicksort(lista.copy())
        end = time.time()
        print(f'Quicksort con tamaño {tamaño}: {end - start:.6f} segundos')

        # Medir tiempo de radix sort
        start = time.time()
        radix_sort(lista.copy())
        end = time.time()
        print(f'Radix sort con tamaño {tamaño}: {end - start:.6f} segundos')

if __name__ == '__main__':
    medir_tiempos()
