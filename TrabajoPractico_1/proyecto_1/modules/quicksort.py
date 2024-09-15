def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quicksort(izquierda) + medio + quicksort(derecha)
# O(n log n) en el caso promedio y O(n^2) en el peor caso, donde n es el número de elementos en la lista.
# El peor caso ocurre cuando el pivote es siempre el menor o mayor elemento, resultando en una partición muy desigual.