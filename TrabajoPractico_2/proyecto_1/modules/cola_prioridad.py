from modules.monticulo import MonticuloBinario

class ColaPrioridad:
    def __init__(self):
        self.__monticulo = MonticuloBinario()

    def insertar(self, elemento):
        """
        Inserta un elemento en la cola de prioridad.
        """
        self.__monticulo.insertar(elemento)

    def atender(self):
        """
        Atiende al elemento con la mayor prioridad (mínimo en el montículo).
        """
        if not self.esta_vacia():
            return self.__monticulo.eliminar_min()
        return None

    def esta_vacia(self):
        """
        Verifica si la cola de prioridad está vacía.
        """
        return self.__monticulo.esta_vacio()

    def tamano(self):
        """
        Devuelve el número de elementos en la cola de prioridad.
        """
        return self.__monticulo.tamano

    def lista_actual(self):
        """
        Devuelve la lista actual de elementos en la cola de prioridad,
        excluyendo el valor inicial ficticio del montículo.
        """
        return self.__monticulo.lista_monticulo[1:]
