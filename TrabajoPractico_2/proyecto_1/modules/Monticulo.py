class MonticuloMinimo:
    def __init__(self):
        self._monticulo = []

    def _padre(self, i):
        return (i - 1) // 2

    def _hijo_izquierdo(self, i):
        return 2 * i + 1

    def _hijo_derecho(self, i):
        return 2 * i + 2

    def insertar(self, paciente):
        self._monticulo.append(paciente)
        self._subir(len(self._monticulo) - 1)

    def _subir(self, i):
        while i > 0 and self._monticulo[i].get_riesgo() < self._monticulo[self._padre(i)].get_riesgo():
            self._monticulo[i], self._monticulo[self._padre(i)] = self._monticulo[self._padre(i)], self._monticulo[i]
            i = self._padre(i)

    def extraer_minimo(self):
        if len(self._monticulo) == 0:
            return None
        if len(self._monticulo) == 1:
            return self._monticulo.pop()
        raiz = self._monticulo[0]
        self._monticulo[0] = self._monticulo.pop()
        self._bajar(0)
        return raiz

    def _bajar(self, i):
        while True:
            hijo_izq = self._hijo_izquierdo(i)
            hijo_der = self._hijo_derecho(i)
            menor = i

            if hijo_izq < len(self._monticulo) and self._monticulo[hijo_izq].get_riesgo() < self._monticulo[menor].get_riesgo():
                menor = hijo_izq
            if hijo_der < len(self._monticulo) and self._monticulo[hijo_der].get_riesgo() < self._monticulo[menor].get_riesgo():
                menor = hijo_der

            if menor == i:
                break
            self._monticulo[i], self._monticulo[menor] = self._monticulo[menor], self._monticulo[i]
            i = menor

    def esta_vacio(self):
        return len(self._monticulo) == 0

    def __len__(self):
        return len(self._monticulo)
