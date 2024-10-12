from typing import List, Dict
from aiohttp import web

from openapi_server.models.mapped_qtl import MappedQTL
from openapi_server.models.qtl import QTL
from openapi_server import util


async def get_mapped_qtlby_position_using_get(request: web.Request, chr, start, stop, map_key) -> web.Response:
    """Returns a list QTL for given position and assembly map

    

    :param chr: Chromosome
    :type chr: str
    :param start: Start Position
    :type start: int
    :param stop: Stop Position
    :type stop: int
    :param map_key: A list of assembly map keys can be found using the lookup service
    :type map_key: int

    """
    return web.Response(status=200)


async def get_qtl_list_by_position_using_get(request: web.Request, chr, start, stop, map_key) -> web.Response:
    """Returns a list QTL for given position and assembly map

    

    :param chr: Chromosome
    :type chr: str
    :param start: Start Position
    :type start: int
    :param stop: Stop Position
    :type stop: int
    :param map_key: A list of assembly map keys can be found using the lookup service
    :type map_key: int

    """
    return web.Response(status=200)


async def get_qtlby_rgd_id_using_get(request: web.Request, rgd_id) -> web.Response:
    """Return a QTL for provided RGD ID

    

    :param rgd_id: RGD ID
    :type rgd_id: int

    """
    return web.Response(status=200)
