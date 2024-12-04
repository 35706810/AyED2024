from random import randint, choices

nombres = [
    'Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina',
    'Carlos', 'Lucía', 'Martín', 'Carolina', 'Fernando', 'Patricia', 'Raúl', 'Soledad',
    'Matías', 'Laura', 'Ricardo', 'Natalia', 'Hernán', 'Florencia', 'Cristian', 'Lorena',
    'Sergio', 'Mariana', 'Pablo', 'Silvana', 'Marcelo', 'Gabriela', 'Facundo', 'Daniela'
]

apellidos = [
    'Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez',
    'Romero', 'Fernández', 'Gómez', 'Sosa', 'Díaz', 'Álvarez', 'Torres', 'Martínez',
    'Ruiz', 'Ramírez', 'Flores', 'Acosta', 'Benítez', 'Silva', 'Ortiz', 'Ledesma',
    'Luna', 'Morales', 'Pereyra', 'Castro', 'Suárez', 'Ríos', 'Ortiz', 'Medina'
]

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self, orden):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo - 1]
        self.__orden = orden

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def riesgo(self):
        return self.__riesgo
    
    @property
    def descripcion_riesgo(self):
        return self.__descripcion

    @property
    def orden(self):
        return self.__orden
    
    def __str__(self):
        cad = f'{self.__orden}: {self.__nombre} {self.__apellido} -> {self.__riesgo}-{self.__descripcion}'
        return cad
     
    def __lt__(self, o):
        if self.__riesgo == o.__riesgo:
            return self.__orden < o.__orden
        else:
            return self.__riesgo < o.__riesgo
