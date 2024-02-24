from alpes.seedwork.aplicacion.servicios import Servicio
from alpes.modulos.vuelos.dominio.entidades import Compania, Reserva

from alpes.modulos.vuelos.infraestructura.fabricas import FabricaRepositorio
from alpes.modulos.vuelos.infraestructura.repositorios import RepositorioReservas
from alpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from alpes.modulos.compania.infraestructura.fabricas import FabricaCompanias
from alpes.modulos.compania.dominio.repositorios import RepositorioCompania
from alpes.modulos.compania.infraestructura.dto import CompaniaModel
from .mapeadores import MapeadorCreacion, MapeadorCreacionRepo, MapeadorReserva

from .dto import CreacionCompaniaDTO 
import asyncio

class ServicioCreacionCompania(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_companias: FabricaCompanias = FabricaCompanias()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_companias(self):
        return self._fabrica_companias
         
    def crear_compania(self, dto: CreacionCompaniaDTO) -> CreacionCompaniaDTO:
        data: Compania = self.fabrica_companias.crear_objeto(dto, MapeadorCreacionRepo())
        data.crear(data)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompania.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, data)
        UnidadTrabajoPuerto.savepoint()
        #AUXILIO
        #UnidadTrabajoPuerto.commit()

        return dto