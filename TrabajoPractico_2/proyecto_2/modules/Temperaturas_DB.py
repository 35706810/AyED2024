from modules.Arbol_AVL import Arbol_AVL
from datetime import datetime

class TemperaturasDB:
    
    def __init__(self):
        # Inicializa la base de datos de temperaturas utilizando un árbol AVL
        self.__arbol_avl = Arbol_AVL()

    def guardar_temperatura(self, temperatura, fecha):
        # Convierte la fecha de string a un objeto datetime y guarda la temperatura en el árbol AVL
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        self.__arbol_avl.agregar(fecha_dt, temperatura)

    def devolver_temperatura(self, fecha):
        # Convierte la fecha de string a datetime y devuelve la temperatura almacenada en esa fecha
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        nodo = self.__arbol_avl.buscar(fecha_dt)
        if nodo:
            return nodo.valor
        return None

    def max_temp_rango(self, fecha1, fecha2):
        # Calcula la temperatura máxima en el rango de fechas proporcionado
        fecha1_dt = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_dt = datetime.strptime(fecha2, "%d/%m/%Y")
        temperaturas = self.__temperaturas_en_rango(fecha1_dt, fecha2_dt)
        if temperaturas:
            return max(temperaturas)
        return None

    def min_temp_rango(self, fecha1, fecha2):
        # Calcula la temperatura mínima en el rango de fechas proporcionado
        fecha1_dt = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_dt = datetime.strptime(fecha2, "%d/%m/%Y")
        temperaturas = self.__temperaturas_en_rango(fecha1_dt, fecha2_dt)
        if temperaturas:
            return min(temperaturas)
        return None

    def temp_extremos_rango(self, fecha1, fecha2):
        # Devuelve tanto la temperatura mínima como la máxima en el rango de fechas proporcionado
        fecha1_dt = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_dt = datetime.strptime(fecha2, "%d/%m/%Y")
        temperaturas = self.__temperaturas_en_rango(fecha1_dt, fecha2_dt)
        if temperaturas:
            return min(temperaturas), max(temperaturas)
        return None, None

    def borrar_temperatura(self, fecha):
        # Elimina la temperatura registrada para la fecha dada
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        self.__arbol_avl.eliminar(fecha_dt)

    def devolver_temperaturas(self, fecha1, fecha2):
        # Devuelve una lista de las temperaturas dentro del rango de fechas especificado
        fecha1_dt = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_dt = datetime.strptime(fecha2, "%d/%m/%Y")
        nodos = self.__nodos_en_rango(fecha1_dt, fecha2_dt)
        return [f"{nodo.clave.strftime('%d/%m/%Y')}: {nodo.valor} ºC" for nodo in nodos]

    def cantidad_muestras(self):
        # Retorna la cantidad total de muestras de temperatura almacenadas en la base de datos
        return self.__arbol_avl.tamano
    
    # Métodos auxiliares para obtener las temperaturas dentro de un rango de fechas.
    def __temperaturas_en_rango(self, fecha1, fecha2):
        # Devuelve una lista de temperaturas en el rango de fechas
        nodos = self.__nodos_en_rango(fecha1, fecha2)
        return [nodo.valor for nodo in nodos]

    def __nodos_en_rango(self, fecha1, fecha2):
        # Devuelve los nodos dentro del rango de fechas dado
        nodos = []
        self.__recorrer_rango(self.__arbol_avl.raiz, fecha1, fecha2, nodos)
        return nodos

    def __recorrer_rango(self, nodo, fecha1, fecha2, nodos):
        # Realiza un recorrido recursivo del árbol AVL para encontrar los nodos dentro del rango de fechas
        if nodo is None:
            return
        if fecha1 <= nodo.clave <= fecha2:
            self.__recorrer_rango(nodo.izquierdo, fecha1, fecha2, nodos)
            nodos.append(nodo)
            self.__recorrer_rango(nodo.derecho, fecha1, fecha2, nodos)
        elif nodo.clave < fecha1:
            self.__recorrer_rango(nodo.derecho, fecha1, fecha2, nodos)
        else:
            self.__recorrer_rango(nodo.izquierdo, fecha1, fecha2, nodos)
