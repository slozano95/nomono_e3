""" Interfaces para los repositorios del dominio de vuelos

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de vuelos

"""

from abc import ABC
from alpes.seedwork.dominio.repositorios import Repositorio

class RepositorioReservas(Repositorio, ABC):
    ...

class RepositorioProveedores(Repositorio, ABC):
    ...

class RepositorioCompanias(Repositorio, ABC):
    ...