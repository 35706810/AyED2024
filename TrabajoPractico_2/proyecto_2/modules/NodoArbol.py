class NodoArbol:
    # Constructor de la clase NodoArbol que inicializa la clave, valor, hijos, padre y factor de equilibrio
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        self.__clave = clave  # La clave que identifica al nodo
        self.__valor = valor  # El valor asociado a la clave del nodo
        self.__izquierdo = izquierdo  # Hijo izquierdo del nodo, por defecto es None
        self.__derecho = derecho  # Hijo derecho del nodo, por defecto es None
        self.__padre = padre  # Nodo padre, por defecto es None
        self.__factorEquilibrio = 0  # Factor de equilibrio para árboles balanceados (AVL)

    # Métodos getters para los atributos privados
    @property
    def clave(self):
        return self.__clave

    @property
    def valor(self):
        return self.__valor

    @property
    def izquierdo(self):
        return self.__izquierdo

    @izquierdo.setter
    def izquierdo(self, valor):
        self.__izquierdo = valor

    @property
    def derecho(self):
        return self.__derecho

    @derecho.setter
    def derecho(self, valor):
        self.__derecho = valor

    @property
    def padre(self):
        return self.__padre

    @padre.setter
    def padre(self, valor):
        self.__padre = valor

    @property
    def factorEquilibrio(self):
        return self.__factorEquilibrio

    @factorEquilibrio.setter
    def factorEquilibrio(self, valor):
        self.__factorEquilibrio = valor

    # Verifica si el nodo tiene hijo izquierdo
    def tieneHijoIzquierdo(self):
        return self.__izquierdo is not None

    # Verifica si el nodo tiene hijo derecho
    def tieneHijoDerecho(self):
        return self.__derecho is not None

    # Verifica si el nodo es hijo izquierdo de su padre
    def esHijoIzquierdo(self):
        return self.__padre and self.__padre.izquierdo == self

    # Verifica si el nodo es hijo derecho de su padre
    def esHijoDerecho(self):
        return self.__padre and self.__padre.derecho == self

    # Verifica si el nodo es la raíz del árbol (no tiene padre)
    def esRaiz(self):
        return self.__padre is None

    # Verifica si el nodo es una hoja (no tiene hijos)
    def esHoja(self):
        return not (self.__derecho or self.__izquierdo)

    # Verifica si el nodo tiene al menos un hijo
    def tieneAlgunHijo(self):
        return self.__derecho or self.__izquierdo

    # Verifica si el nodo tiene ambos hijos (izquierdo y derecho)
    def tieneAmbosHijos(self):
        return self.__derecho and self.__izquierdo

    # Reemplaza los datos de un nodo (clave, valor, hijos izquierdo y derecho)
    def reemplazarDatoDeNodo(self, clave, valor, izquierdo, derecho):
        self.__clave = clave  # Asigna nueva clave
        self.__valor = valor  # Asigna nuevo valor
        self.__izquierdo = izquierdo  # Asigna nuevo hijo izquierdo
        self.__derecho = derecho  # Asigna nuevo hijo derecho
        
        # Actualiza los padres de los hijos si existen
        if self.tieneHijoIzquierdo():
            self.__izquierdo.padre = self
        if self.tieneHijoDerecho():
            self.__derecho.padre = self
