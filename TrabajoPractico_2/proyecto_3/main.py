from modules.grafo import cargar_grafo
from modules.algoritmo_prim import prim, calcular_sumas_distancias

def imprimir_recorrido_mst(mst, inicio):
    visitados = set()
    cola = [(inicio, None)]
    visitados.add(inicio)

    print("Recorrido del mensaje:")
    while cola:
        actual, predecesor = cola.pop(0)
        if predecesor is None:
            print(f"{actual} es la aldea de inicio.")
        else:
            print(f"{predecesor} envía la noticia a {actual}.")

        for vecino in [aldea for aldea, pred in mst.items() if pred and pred.nombre == actual and aldea not in visitados]:
            cola.append((vecino, actual))
            visitados.add(vecino)

def mostrar_aldeas_alfabeticamente(grafo):
    aldeas_ordenadas = sorted(grafo.vertices.keys())
    print("Aldeas en orden alfabético:")
    for aldea in aldeas_ordenadas:
        print(aldea)

def main():
    grafo = cargar_grafo("data/aldeas.txt")
    mostrar_aldeas_alfabeticamente(grafo)
    aldea_inicio = "Peligros"
    mst = prim(grafo, aldea_inicio)

    suma_distancias, suma_total = calcular_sumas_distancias(grafo, mst)
    print(f"Suma total de distancias: {suma_total}")
    imprimir_recorrido_mst(mst, aldea_inicio)

if __name__ == "__main__":
    main()
