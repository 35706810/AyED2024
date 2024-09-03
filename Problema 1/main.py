import random
import time
import matplotlib.pyplot as plt
from burbuja import burbuja
from quicksort import quicksort
from radix_sort import radix_sort

# Función para medir los tiempos de ejecución
def medir_tiempos():
    tamaños = range(1, 1001)
    tiempos_burbuja = []
    tiempos_quicksort = []
    tiempos_radix = []
    tiempos_sorted = []

    for tamaño in tamaños:
        lista = [random.randint(0, 99999) for _ in range(tamaño)]

        # Medir tiempo de burbuja
        if tamaño <= 1000:
            start = time.time()
            burbuja(lista.copy())
            end = time.time()
            tiempos_burbuja.append(end - start)
        else:
            tiempos_burbuja.append(None)

        # Medir tiempo de quicksort
        start = time.time()
        quicksort(lista.copy())
        end = time.time()
        tiempos_quicksort.append(end - start)

        # Medir tiempo de radix sort
        start = time.time()
        radix_sort(lista.copy())
        end = time.time()
        tiempos_radix.append(end - start)

        # Medir tiempo de sorted (función built-in)
        start = time.time()
        sorted(lista.copy())
        end = time.time()
        tiempos_sorted.append(end - start)

    return tamaños, tiempos_burbuja, tiempos_quicksort, tiempos_radix, tiempos_sorted

# Graficar los tiempos
def graficar_tiempos(tamaños, tiempos_burbuja, tiempos_quicksort, tiempos_radix, tiempos_sorted):
    plt.figure(figsize=(10, 6))
    plt.plot(tamaños, tiempos_burbuja, label='Burbuja')
    plt.plot(tamaños, tiempos_quicksort, label='Quicksort')
    plt.plot(tamaños, tiempos_radix, label='Radix Sort')
    plt.plot(tamaños, tiempos_sorted, label='Sorted (built-in)')
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación de tiempos de ejecución de algoritmos de ordenamiento')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    tamaños, tiempos_burbuja, tiempos_quicksort, tiempos_radix, tiempos_sorted = medir_tiempos()
    graficar_tiempos(tamaños, tiempos_burbuja, tiempos_quicksort, tiempos_radix, tiempos_sorted)
