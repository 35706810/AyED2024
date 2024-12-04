from modules.NodoArbol import NodoArbol

class Arbol_AVL:
    def __init__(self):
        self.__raiz = None  # Inicializa el árbol vacío
        self.__tamano = 0

    @property
    def raiz(self):
        return self.__raiz

    @property
    def tamano(self):
        return self.__tamano

    def agregar(self, clave, valor):
        if self.__raiz:
            self.__agregar_recursivo(clave, valor, self.__raiz)
        else:
            self.__raiz = NodoArbol(clave, valor)
        self.__tamano += 1

    def __agregar_recursivo(self, clave, valor, nodo_actual):
        if clave < nodo_actual.clave:
            if nodo_actual.tieneHijoIzquierdo():
                self.__agregar_recursivo(clave, valor, nodo_actual.izquierdo)
            else:
                nodo_actual.izquierdo = NodoArbol(clave, valor, padre=nodo_actual)
                self.__actualizar_equilibrio(nodo_actual.izquierdo)
        else:
            if nodo_actual.tieneHijoDerecho():
                self.__agregar_recursivo(clave, valor, nodo_actual.derecho)
            else:
                nodo_actual.derecho = NodoArbol(clave, valor, padre=nodo_actual)
                self.__actualizar_equilibrio(nodo_actual.derecho)

    def __actualizar_equilibrio(self, nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.__reequilibrar(nodo)
            return
        if nodo.padre is not None:
            if nodo.esHijoIzquierdo():
                nodo.padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho():
                nodo.padre.factorEquilibrio -= 1
            if nodo.padre.factorEquilibrio != 0:
                self.__actualizar_equilibrio(nodo.padre)

    def __rotar_izquierda(self, rot_raiz):
        nueva_raiz = rot_raiz.derecho
        rot_raiz.derecho = nueva_raiz.izquierdo
        if nueva_raiz.izquierdo:
            nueva_raiz.izquierdo.padre = rot_raiz
        nueva_raiz.padre = rot_raiz.padre
        if rot_raiz.esRaiz():
            self.__raiz = nueva_raiz
        else:
            if rot_raiz.esHijoIzquierdo():
                rot_raiz.padre.izquierdo = nueva_raiz
            else:
                rot_raiz.padre.derecho = nueva_raiz
        nueva_raiz.izquierdo = rot_raiz
        rot_raiz.padre = nueva_raiz
        rot_raiz.factorEquilibrio += 1 - min(nueva_raiz.factorEquilibrio, 0)
        nueva_raiz.factorEquilibrio += 1 + max(rot_raiz.factorEquilibrio, 0)

    def __rotar_derecha(self, rot_raiz):
        nueva_raiz = rot_raiz.izquierdo
        rot_raiz.izquierdo = nueva_raiz.derecho
        if nueva_raiz.derecho:
            nueva_raiz.derecho.padre = rot_raiz
        nueva_raiz.padre = rot_raiz.padre
        if rot_raiz.esRaiz():
            self.__raiz = nueva_raiz
        else:
            if rot_raiz.esHijoDerecho():
                rot_raiz.padre.derecho = nueva_raiz
            else:
                rot_raiz.padre.izquierdo = nueva_raiz
        nueva_raiz.derecho = rot_raiz
        rot_raiz.padre = nueva_raiz
        rot_raiz.factorEquilibrio -= 1 - max(nueva_raiz.factorEquilibrio, 0)
        nueva_raiz.factorEquilibrio -= 1 + min(rot_raiz.factorEquilibrio, 0)

    def __reequilibrar(self, nodo):
        if nodo.factorEquilibrio < 0:
            if nodo.derecho.factorEquilibrio > 0:
                self.__rotar_derecha(nodo.derecho)
            self.__rotar_izquierda(nodo)
        elif nodo.factorEquilibrio > 0:
            if nodo.izquierdo.factorEquilibrio < 0:
                self.__rotar_izquierda(nodo.izquierdo)
            self.__rotar_derecha(nodo)

    def buscar(self, clave):
        return self.__buscar_recursivo(clave, self.__raiz)

    def __buscar_recursivo(self, clave, nodo):
        if nodo is None:
            return None
        if clave == nodo.clave:
            return nodo
        elif clave < nodo.clave:
            return self.__buscar_recursivo(clave, nodo.izquierdo)
        else:
            return self.__buscar_recursivo(clave, nodo.derecho)

    def eliminar(self, clave):
        nodo_eliminado = self.__eliminar_recursivo(clave, self.__raiz)
        if nodo_eliminado is not None:
            self.__tamano -= 1

    def __eliminar_recursivo(self, clave, nodo):
        if nodo is None:
            return nodo
        if clave < nodo.clave:
            nodo.izquierdo = self.__eliminar_recursivo(clave, nodo.izquierdo)
        elif clave > nodo.clave:
            nodo.derecho = self.__eliminar_recursivo(clave, nodo.derecho)
        else:
            if nodo.tieneAmbosHijos():
                sucesor = self.__encontrar_minimo(nodo.derecho)
                nodo.clave, nodo.valor = sucesor.clave, sucesor.valor
                nodo.derecho = self.__eliminar_recursivo(sucesor.clave, nodo.derecho)
            else:
                nodo = nodo.izquierdo if nodo.tieneHijoIzquierdo() else nodo.derecho
        if nodo is None:
            return nodo
        self.__actualizar_equilibrio_post_eliminacion(nodo)
        return nodo

    def __actualizar_equilibrio_post_eliminacion(self, nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.__reequilibrar(nodo)
            return
        if nodo.padre is not None:
            if nodo.esHijoIzquierdo():
                nodo.padre.factorEquilibrio -= 1
            elif nodo.esHijoDerecho():
                nodo.padre.factorEquilibrio += 1
            if nodo.padre.factorEquilibrio != 0:
                self.__actualizar_equilibrio_post_eliminacion(nodo.padre)

    def __encontrar_minimo(self, nodo):
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo
