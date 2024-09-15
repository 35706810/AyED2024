import random
import time
import matplotlib.pyplot as plt

from modules.burbuja import burbuja
from modules.quicksort import quicksort
from modules.radix_sort import radix_sort

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
            tiempos_burbuja.append((end - start) * 1000)  # Convertir a milisegundos
        else:
            tiempos_burbuja.append(None)

        # Medir tiempo de quicksort
        start = time.time()
        quicksort(lista.copy())
        end = time.time()
        tiempos_quicksort.append((end - start) * 1000)  # Convertir a milisegundos

        # Medir tiempo de radix sort
        start = time.time()
        radix_sort(lista.copy())
        end = time.time()
        tiempos_radix.append((end - start) * 1000)  # Convertir a milisegundos

        # Medir tiempo de sorted (función built-in)
        start = time.time()
        sorted(lista.copy())
        end = time.time()
        tiempos_sorted.append((end - start) * 1000)  # Convertir a milisegundos

    return tamaños, tiempos_burbuja, tiempos_quicksort, tiempos_radix, tiempos_sorted

# Graficar los tiempos
def graficar_tiempos(tamaños, tiempos_burbuja, tiempos_quicksort, tiempos_radix, tiempos_sorted):
    plt.figure(figsize=(12, 8))
    plt.plot(tamaños, tiempos_burbuja, label='Burbuja (ms)')
    plt.plot(tamaños, tiempos_quicksort, label='Quicksort (ms)')
    plt.plot(tamaños, tiempos_radix, label='Radix Sort (ms)')
    plt.plot(tamaños, tiempos_sorted, label='Sorted (built-in) (ms)')
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo de ejecución (milisegundos)')
    plt.title('Comparación de tiempos de ejecución de algoritmos de ordenamiento')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    tamaños, tiempos_burbuja, tiempos_quicksort, tiempos_radix, tiempos_sorted = medir_tiempos()
    
    # Imprimir tiempos de ejecución totales en consola
    promedio_burbuja = [t for t in tiempos_burbuja if t is not None]
    print(f"Tiempo promedio de Burbuja: {sum(promedio_burbuja) / len(promedio_burbuja):.2f} ms" if promedio_burbuja else "Burbuja no medido para tamaños mayores a 1000")

    promedio_quicksort = sum(tiempos_quicksort) / len(tiempos_quicksort)
    print(f"Tiempo promedio de Quicksort: {promedio_quicksort:.2f} ms")

    promedio_radix = sum(tiempos_radix) / len(tiempos_radix)
    print(f"Tiempo promedio de Radix Sort: {promedio_radix:.2f} ms")

    promedio_sorted = sum(tiempos_sorted) / len(tiempos_sorted)
    print(f"Tiempo promedio de Sorted (built-in): {promedio_sorted:.2f} ms")

    graficar_tiempos(tamaños, tiempos_burbuja, tiempos_quicksort, tiempos_radix, tiempos_sorted)
