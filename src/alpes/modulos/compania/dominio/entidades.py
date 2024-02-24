from __future__ import annotations
from dataclasses import dataclass, field
import uuid

import alpes.modulos.vuelos.dominio.objetos_valor as ov
from alpes.modulos.vuelos.dominio.eventos import ReservaCreada, ReservaAprobada, ReservaCancelada, ReservaPagada
from alpes.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class Compania(Entidad):
    id: str
    nombre: str
    
# @dataclass
# class Compania(AgregacionRaiz):
#     id_cliente: uuid.UUID = field(hash=True, default=None)
#     nombre: ov.EstadoReserva = field(default=ov.EstadoReserva.PENDIENTE)
#     itinerarios: list[ov.Itinerario] = field(default_factory=list[ov.Itinerario])

#     def crear_reserva(self, compania: Compania):
#         self.id = compania.id
#         self.nombre = compania.nombre
#         self.agregar_evento(ReservaCreada(id_reserva=self.id, id_cliente=self.id_cliente, estado=self.estado.name, fecha_creacion=self.fecha_creacion))
