import math

class MonticuloBinario: 
    """
    Montículo Binario Mínimo en el que la clave más pequeña está siempre en el frente, 
    pues los niveles de gravedad van de 1 a 3.
    """
    def __init__(self):
        self.__lista_monticulo = [-math.inf]  # Elemento inicial ficticio para simplificar los cálculos de índices
        self.__tamano_actual = 0

    # Métodos privados (detalles internos de implementación)
    def __infilt_arriba(self, i): 
        """
        Subir un elemento en el montículo para mantener la propiedad del montículo mínimo.
        """
        while i // 2 > 0:
            if self.__lista_monticulo[i] < self.__lista_monticulo[i // 2]:
                self.__lista_monticulo[i], self.__lista_monticulo[i // 2] = self.__lista_monticulo[i // 2], self.__lista_monticulo[i]
            i = i // 2

    def __infilt_abajo(self, i): 
        """
        Bajar un elemento en el montículo para mantener la propiedad del montículo mínimo.
        """
        while (i * 2) <= self.__tamano_actual:
            hm = self.__hijo_min(i)
            if self.__lista_monticulo[i] > self.__lista_monticulo[hm]:
                self.__lista_monticulo[i], self.__lista_monticulo[hm] = self.__lista_monticulo[hm], self.__lista_monticulo[i]
            i = hm
            
    def __hijo_min(self, i): 
        """
        Determinar el índice del hijo menor de un nodo.
        """
        if i * 2 + 1 > self.__tamano_actual:
            return i * 2
        else:
            if self.__lista_monticulo[i * 2] < self.__lista_monticulo[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    # Métodos públicos (interfaz de usuario)
    def insertar(self, k):
        """
        Agregar un elemento al montículo.
        Recibe un elemento k.
        """ 
        self.__lista_monticulo.append(k)
        self.__tamano_actual += 1
        self.__infilt_arriba(self.__tamano_actual)

    def eliminar_min(self): 
        """
        Eliminar y devolver el valor mínimo del montículo (la raíz).
        """
        if self.esta_vacio():
            raise IndexError("No se puede eliminar de un montículo vacío.")
        
        valor_sacado = self.__lista_monticulo[1]
        self.__lista_monticulo[1] = self.__lista_monticulo[self.__tamano_actual]
        self.__tamano_actual -= 1
        self.__lista_monticulo.pop()
        self.__infilt_abajo(1)
        return valor_sacado
    
    def buscar_min(self): 
        """
        Devolver el valor mínimo del montículo sin eliminarlo.
        """
        if self.esta_vacio():
            return None
        return self.__lista_monticulo[1]
        
    def esta_vacio(self): 
        """
        Devolver True si el montículo está vacío, False en caso contrario.
        """
        return self.__tamano_actual == 0

    def construir_monticulo(self, una_lista): 
        """
        Organizar una lista inicial en forma de montículo.
        """
        i = len(una_lista) // 2
        self.__tamano_actual = len(una_lista)
        self.__lista_monticulo = [-math.inf] + una_lista[:]  # Mantener el primer elemento ficticio
        while i > 0:
            self.__infilt_abajo(i)
            i -= 1

    # Propiedades públicas
    @property
    def tamano(self):
        """
        Tamaño actual del montículo.
        """ 
        return self.__tamano_actual

    @property
    def lista_monticulo(self):
        """
        Copia de la lista interna del montículo.
        """
        return self.__lista_monticulo.copy()

    