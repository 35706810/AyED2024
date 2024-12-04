from modules.paciente import Paciente
from modules.cola_prioridad import ColaPrioridad
import time
import datetime
import random

# Inicialización de la cola de espera y el contador de pacientes
cola_de_espera = ColaPrioridad()
numero_pacientes = 20  
contador = 0  

# Ciclo principal de la simulación
while contador < numero_pacientes or not cola_de_espera.esta_vacia():
    # Obtener la fecha y hora actual
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-' * 15)
    print('\n', fecha_y_hora, '\n')

    # Crear y agregar un nuevo paciente si no se ha alcanzado el límite
    if contador < numero_pacientes:
        paciente = Paciente(contador)  
        cola_de_espera.insertar(paciente) 
        contador += 1  

    # Atender al paciente en este ciclo con un 50% de probabilidad
    if random.random() < 0.5:
        paciente_atendido = cola_de_espera.atender()  # Atender al paciente con mayor prioridad
        if paciente_atendido:
            print('*' * 40)
            print('Se atiende el paciente:', paciente_atendido)  # Mostrar información del paciente atendido
            print('*' * 40)

    print()

    # Mostrar el número de pacientes restantes en la cola
    print('Pacientes que faltan atenderse:', cola_de_espera.tamano())
    
    # Crear una copia de la lista de pacientes para visualización
    pacientes_visibles = cola_de_espera.lista_actual()
    
    # Mostrar información de los pacientes en espera
    for paciente in pacientes_visibles:
        print('\t', paciente)

    print()
    print('-*-' * 15)

    time.sleep(0.5)  # Esperar medio segundo antes del siguiente ciclo

print("No hay más pacientes por atender. Fin de la simulación.")


