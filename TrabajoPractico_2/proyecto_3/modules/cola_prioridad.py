from modules.monticulo import MonticuloBinario

class ColaPrioridad:
    """Define una cola de prioridad mínima utilizando un montículo binario."""
    def __init__(self):
        self.monticulo = MonticuloBinario()

    def insertar(self, vertice):
        """Inserta un vértice en la cola de prioridad."""
        self.monticulo.insertar(vertice)

    def eliminar_min(self):
        """Elimina y retorna el vértice con la menor distancia."""
        return self.monticulo.eliminar_min()

    def construir_monticulo(self, lista):
        """Construye el montículo inicial a partir de una lista de vértices."""
        self.monticulo.construir_monticulo(lista)

    def esta_vacio(self):
        """Verifica si la cola de prioridad está vacía."""
        return self.monticulo.esta_vacio()

    def actualizar_distancia(self, vertice, nueva_distancia):
        """Actualiza la distancia de un vértice y ajusta su posición en el montículo."""
        self.monticulo.actualizar_distancia(vertice, nueva_distancia)
