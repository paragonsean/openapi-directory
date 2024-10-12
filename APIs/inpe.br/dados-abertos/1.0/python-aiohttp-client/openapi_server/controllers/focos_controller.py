from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_focos_count_resource(request: web.Request, pais_id=None, estado_id=None, municipio_id=None, satelite=None) -> web.Response:
    """Endpoint para retorno da contagem dos focos de calor

    

    :param pais_id: Código do país pelo qual será filtrado o resultado. Ver rotas auxiliares.
    :type pais_id: int
    :param estado_id: Código do estado pelo qual será filtrado o resultado. Ver rotas auxiliares.
    :type estado_id: int
    :param municipio_id: Código do município pelo qual será filtrado o resultado. Ver rotas auxiliares.
    :type municipio_id: int
    :param satelite: Nome do satélte pelo qual será filtrado o resultado. Ver rotas auxiliares.
    :type satelite: List[str]

    """
    return web.Response(status=200)


async def get_focos_resource(request: web.Request, pais_id=None, estado_id=None, municipio_id=None, satelite=None, x_fields=None) -> web.Response:
    """Endpoint para retorno dos dados de focos de calor

    

    :param pais_id: Código do país pelo qual será filtrado o resultado. Ver rotas auxiliares.
    :type pais_id: int
    :param estado_id: Código do estado pelo qual será filtrado o resultado. Ver rotas auxiliares.
    :type estado_id: int
    :param municipio_id: Código do município pelo qual será filtrado o resultado. Ver rotas auxiliares.
    :type municipio_id: int
    :param satelite: Nome do satélte pelo qual será filtrado o resultado. Ver rotas auxiliares.
    :type satelite: List[str]
    :param x_fields: An optional fields mask
    :type x_fields: str

    """
    return web.Response(status=200)
