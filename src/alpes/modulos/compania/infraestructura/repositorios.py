
from alpes.config.db import db
from alpes.modulos.vuelos.dominio.repositorios import RepositorioReservas, RepositorioProveedores
from alpes.modulos.vuelos.dominio.objetos_valor import NombreAero, Odo, Leg, Segmento, Itinerario, CodigoIATA
from alpes.modulos.vuelos.dominio.entidades import Compania, Proveedor, Aeropuerto, Reserva
from alpes.modulos.vuelos.dominio.fabricas import FabricaVuelos
from alpes.modulos.compania.dominio.repositorios import RepositorioCompania

from uuid import UUID

from alpes.modulos.compania.aplicacion.mapeadores import MapeadorCreacionRepo

class RepositorioCompaniasSQL(RepositorioCompania):

    def __init__(self):
        pass
        
    
    def obtener_por_id(self, id: UUID) -> Compania:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Compania]:
        return []

    def agregar(self, entity: Compania):
        dto = MapeadorCreacionRepo().entidad_a_dto(entidad=entity)
        db.session.add(dto)

    def actualizar(self, entity: Compania):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError