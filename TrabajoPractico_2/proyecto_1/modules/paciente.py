# -*- coding: utf-8 -*-

from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
probabilidades = [0.1, 0.3, 0.6]  # Probabilidades para los niveles de riesgo

class Paciente:
    contador_pacientes = 0

    def __init__(self):
        Paciente.contador_pacientes += 1
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        self.__numero_orden = Paciente.contador_pacientes  # Asigna número único al paciente

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo

    def get_numero_orden(self):
        return self.__numero_orden  # Nuevo método para obtener el número de orden
    
    def get_descripcion_riesgo(self):
        return self.__descripcion
    
    def __str__(self):
        cad = f"{self.__nombre} {self.__apellido}\t -> {self.__riesgo}-{self.__descripcion} (Nº {self.__numero_orden})"
        return cad
