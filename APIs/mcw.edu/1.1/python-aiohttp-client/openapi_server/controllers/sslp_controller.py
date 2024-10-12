from typing import List, Dict
from aiohttp import web

from openapi_server.models.mapped_sslp import MappedSSLP
from openapi_server import util


async def get_mapped_sslpby_position_using_get(request: web.Request, chr, start, stop, map_key) -> web.Response:
    """Returns a list SSLP for given position and assembly map

    

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
