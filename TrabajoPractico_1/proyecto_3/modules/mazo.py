from ListaDobleEnlazada import ListaDobleEnlazada

# Definir la excepción DequeEmptyError
class DequeEmptyError(Exception):
    pass

class Mazo:
    def __init__(self):
        self.cartas = ListaDobleEnlazada()

    def __len__(self):
        # Devuelve la cantidad de cartas en el mazo
        return len(self.cartas)

    def poner_carta_arriba(self, carta):
        # Agrega una carta al inicio del mazo (la parte superior)
        self.cartas.agregar_al_inicio(carta)

    def poner_carta_abajo(self, carta):
        # Agrega una carta al final del mazo (la parte inferior)
        self.cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        # Extrae una carta del inicio del mazo (la parte superior)
        if len(self.cartas) == 0:
            raise DequeEmptyError("No hay cartas en el mazo.")
        
        carta = self.cartas.extraer(0)  # Extrae la primera carta
        if mostrar:
            carta.visible = True
        return carta

    def sacar_carta_abajo(self):
        # Extrae una carta del final del mazo (la parte inferior)
        if len(self.cartas) == 0:
            raise DequeEmptyError("No hay cartas en el mazo.")
        
        return self.cartas.extraer()  # Extrae la última carta

    def __str__(self):
        # Muestra las cartas del mazo en el formato adecuado
        return " ".join([str(carta) for carta in self.cartas])
