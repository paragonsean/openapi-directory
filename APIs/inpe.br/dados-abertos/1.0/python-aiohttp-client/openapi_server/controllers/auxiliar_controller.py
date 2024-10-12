from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_estados_auxiliar_resource(request: web.Request, pais_id=None) -> web.Response:
    """Endpoint para retorno dos dados de estados utilizados na filtragem de focos

    

    :param pais_id: Código do país pelo qual será filtrado o resultado. Ver rotas auxiliares.
    :type pais_id: List[int]

    """
    return web.Response(status=200)


async def get_municipios_auxiliar_resource(request: web.Request, pais_id, estado_id=None) -> web.Response:
    """Endpoint para retorno dos dados de municípios utilizados na filtragem de focos

    

    :param pais_id: Código do país pelo qual será filtrado o resultado. Ver rotas auxiliares.
    :type pais_id: int
    :param estado_id: Código do estado pelo qual será filtrado o resultado. Ver rotas auxiliares.
    :type estado_id: List[int]

    """
    return web.Response(status=200)


async def get_paises_auxiliar_resource(request: web.Request, ) -> web.Response:
    """Endpoint para retorno dos dados de países utilizados na filtragem de focos

    


    """
    return web.Response(status=200)


async def get_satelite_auxiliar_resource(request: web.Request, ) -> web.Response:
    """Endpoint para retorno dos dados de satélites utilizados na filtragem de focos

    


    """
    return web.Response(status=200)
