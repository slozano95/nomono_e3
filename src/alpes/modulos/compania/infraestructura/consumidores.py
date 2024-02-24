import logging
import traceback
from alpes.seedwork.infraestructura import utils
from alpes.modulos.vuelos.infraestructura.schema.v1.comandos import ComandoCrearReserva

import pulsar,_pulsar
from pulsar.schema import *

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-compania', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='aeroalpes-sub-eventos', schema=AvroSchema(ComandoCrearReserva))
        logging.info('OK: Suscribiendose al tópico de eventos compania!')
        while True:
            mensaje = consumidor.receive()
            print(f'Evento compania recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos compania!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-compania', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='aeroalpes-sub-comandos', schema=AvroSchema(ComandoCrearReserva))
        logging.info('OK: Suscribiendose al tópico de comandos compania!')
        while True:
            mensaje = consumidor.receive()
            print(f'Comando compania recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos compania!')
        traceback.print_exc()
        if cliente:
            cliente.close()