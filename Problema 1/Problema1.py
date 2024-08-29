import random
import time

def burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quicksort(izquierda) + medio + quicksort(derecha)

def radix_sort(lista):
    max_val = max(lista)
    exp = 1
    while max_val // exp > 0:
        counting_sort(lista, exp)
        exp *= 10
    return lista

def counting_sort(lista, exp):
    n = len(lista)
    salida = [0] * n
    conteo = [0] * 10

    for i in range(n):
        indice = (lista[i] // exp) % 10
        conteo[indice] += 1

    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    for i in range(n - 1, -1, -1):
        indice = (lista[i] // exp) % 10
        salida[conteo[indice] - 1] = lista[i]
        conteo[indice] -= 1

    for i in range(n):
        lista[i] = salida[i]

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
