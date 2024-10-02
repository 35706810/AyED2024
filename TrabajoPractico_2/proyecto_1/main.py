# -*- coding: utf-8 -*-
"""
Sala de emergencias
"""

import time
import datetime
import modules.paciente as pac
import modules.Monticulo as mont
import random

n = 20  # cantidad de ciclos de simulación

monticulo_pacientes = mont.MonticuloMinimo()

# Ciclo que gestiona la simulación
for i in range(n):
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente
    paciente = pac.Paciente()
    monticulo_pacientes.insertar(paciente)
    print('Paciente ingresado:', paciente)

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5:
        # Se atiende al paciente con menor riesgo y más antiguo
        paciente_atendido = monticulo_pacientes.extraer_minimo()
        print('*'*40)
        print('Se atiende al paciente:', paciente_atendido)
        print('*'*40)
    else:
        pass
    
    print()

    # Mostrar pacientes restantes en el montículo
    print('Pacientes que faltan atenderse:', len(monticulo_pacientes))
    for paciente in monticulo_pacientes._monticulo:
        print('\t', paciente)
    
    print()
    print('-*-'*15)
    
    time.sleep(1)

