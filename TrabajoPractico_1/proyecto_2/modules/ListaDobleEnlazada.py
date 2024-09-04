class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def __len__(self):
        return self.tamanio

    def __iter__(self):
        nodo = self.cabeza
        while nodo:
            yield nodo.dato
            nodo = nodo.siguiente

    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamanio += 1

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cola is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamanio += 1

    def insertar(self, dato, posicion):
        if posicion < -self.tamanio or posicion > self.tamanio:
            raise Exception("Posición inválida")

        if posicion < 0:
            posicion = self.tamanio + posicion

        nuevo_nodo = Nodo(dato)

        if posicion == 0:
            self.agregar_al_inicio(dato)
        elif posicion == self.tamanio:
            self.agregar_al_final(dato)
        else:
            nodo_actual = self.cabeza
            for _ in range(posicion - 1):
                nodo_actual = nodo_actual.siguiente

            nuevo_nodo.siguiente = nodo_actual.siguiente
            nuevo_nodo.anterior = nodo_actual
            nodo_actual.siguiente.anterior = nuevo_nodo
            nodo_actual.siguiente = nuevo_nodo

            self.tamanio += 1

    def extraer(self, posicion=None):
        if self.tamanio == 0:
            raise Exception("La lista está vacía")

        if posicion is None:
            posicion = self.tamanio - 1
        else:
            if posicion < 0:
                posicion = self.tamanio + posicion

            if posicion < 0 or posicion >= self.tamanio:
                raise Exception("Posición inválida")

        if posicion == 0:
            valor = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
        elif posicion == self.tamanio - 1:
            valor = self.cola.dato
            self.cola = self.cola.anterior
            if self.cola:
                self.cola.siguiente = None
            else:
                self.cabeza = None
        else:
            nodo_actual = self.cabeza
            for _ in range(posicion):
                nodo_actual = nodo_actual.siguiente

            valor = nodo_actual.dato
            nodo_actual.anterior.siguiente = nodo_actual.siguiente
            nodo_actual.siguiente.anterior = nodo_actual.anterior

        self.tamanio -= 1
        return valor

    def copiar(self):
        lista_copia = ListaDobleEnlazada()
        nodo_actual = self.cabeza
        while nodo_actual:
            lista_copia.agregar_al_final(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        return lista_copia

    def invertir(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            nodo_actual.siguiente, nodo_actual.anterior = nodo_actual.anterior, nodo_actual.siguiente
            nodo_actual = nodo_actual.anterior
        self.cabeza, self.cola = self.cola, self.cabeza

    def concatenar(self, otra_lista):
        if otra_lista.cabeza is None:
            return

        if self.cabeza is None:
         
            self.cabeza = otra_lista.cabeza
            self.cola = otra_lista.cola
        else:
           
            self.cola.siguiente = otra_lista.cabeza
            otra_lista.cabeza.anterior = self.cola
            self.cola = otra_lista.cola

        self.tamanio += otra_lista.tamanio

        otra_lista.cabeza = None
        otra_lista.cola = None
        otra_lista.tamanio = 0


    def __add__(self, otra_lista):
        nueva_lista = ListaDobleEnlazada()
        
       
        nodo_actual = self.cabeza
        while nodo_actual:
            nueva_lista.agregar_al_final(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        
        
        nodo_actual = otra_lista.cabeza
        while nodo_actual:
            nueva_lista.agregar_al_final(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        
        return nueva_lista




