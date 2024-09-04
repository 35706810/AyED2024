# medir_tiempos.py

import time
import matplotlib.pyplot as plt
from modules import ListaDobleEnlazada

def medir_tiempos():
    tamanios = []
    tiempos_len = []
    tiempos_copiar = []
    tiempos_invertir = []

    for n in range(1, 1001, 100):  # Ajusta el rango según sea necesario
        lista = ListaDobleEnlazada()
        for i in range(n):
            lista.agregar_al_final(i)
        
        tamanios.append(n)
        
        # Medir tiempo de len
        start_time = time.time()
        len(lista)
        end_time = time.time()
        tiempos_len.append(end_time - start_time)
        
        # Medir tiempo de copiar
        start_time = time.time()
        lista_copia = lista.copiar()
        end_time = time.time()
        tiempos_copiar.append(end_time - start_time)
        
        # Medir tiempo de invertir
        start_time = time.time()
        lista.invertir()
        end_time = time.time()
        tiempos_invertir.append(end_time - start_time)
    
    return tamanios, tiempos_len, tiempos_copiar, tiempos_invertir

# Ejecutar la medición y graficar
tamanios, tiempos_len, tiempos_copiar, tiempos_invertir = medir_tiempos()

plt.figure(figsize=(12, 8))
plt.plot(tamanios, tiempos_len, label='len', marker='o')
plt.plot(tamanios, tiempos_copiar, label='copiar', marker='o')
plt.plot(tamanios, tiempos_invertir, label='invertir', marker='o')
plt.xlabel('Tamaño de la lista (N)')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Tiempo de ejecución vs Tamaño de la lista')
plt.legend()
plt.grid(True)
plt.show()
