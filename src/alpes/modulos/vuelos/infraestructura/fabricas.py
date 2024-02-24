""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field
from alpes.seedwork.dominio.fabricas import Fabrica
from alpes.seedwork.dominio.repositorios import Repositorio
from alpes.modulos.vuelos.dominio.repositorios import RepositorioCompanias, RepositorioProveedores, RepositorioReservas
from alpes.modulos.compania.infraestructura.repositorios import RepositorioCompaniasSQL
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioCompanias.__class__:
            return RepositorioCompaniasSQL()
        else:
            raise ExcepcionFabrica()