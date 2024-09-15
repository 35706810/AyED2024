from modules.ListaDobleEnlazada import ListaDobleEnlazada

# Definir la excepción DequeEmptyError
class DequeEmptyError(Exception):
    pass

class Mazo:
    def __init__(self):
        # Inicializa un mazo vacío usando una lista doblemente enlazada
        self.mazo = ListaDobleEnlazada()

    def __len__(self):
        # Devuelve la cantidad de cartas en el mazo.
        # Complejidad: O(1) ya que la longitud se almacena y se puede acceder de manera directa.
        return len(self.mazo)

    def poner_carta_arriba(self, carta):
        # Agrega una carta al inicio del mazo (la parte superior).
        # Complejidad: O(1) ya que se agrega al inicio de la lista doblemente enlazada sin necesidad de recorrerla.
        self.mazo.agregar_al_inicio(carta)

    def poner_carta_abajo(self, carta):
        # Agrega una carta al final del mazo (la parte inferior).
        # Complejidad: O(1) ya que se agrega al final de la lista doblemente enlazada sin necesidad de recorrerla.
        self.mazo.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        # Extrae una carta del inicio del mazo (la parte superior).
        # Complejidad: O(1) ya que se elimina del inicio de la lista doblemente enlazada sin necesidad de recorrerla.
        if len(self.mazo) == 0:
            raise DequeEmptyError("No hay cartas en el mazo.")
        
        carta = self.mazo.extraer(0)
        if mostrar:
            carta.visible = True
        return carta

    def sacar_carta_abajo(self):
        # Extrae una carta del final del mazo (la parte inferior).
        # Complejidad: O(1) ya que se elimina del final de la lista doblemente enlazada sin necesidad de recorrerla.
        if len(self.mazo) == 0:
            raise DequeEmptyError("No hay cartas en el mazo.")
        
        return self.mazo.extraer()

    def __str__(self):
        # Muestra las cartas del mazo en el formato adecuado.
        # Complejidad: O(n) donde n es el número de cartas en el mazo, ya que debe recorrer todas las cartas para crear la representación en cadena.
        return " ".join([str(carta) for carta in self.mazo])

