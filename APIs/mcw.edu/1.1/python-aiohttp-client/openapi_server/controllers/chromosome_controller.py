from typing import List, Dict
from aiohttp import web

from openapi_server.models.chromosome import Chromosome
from openapi_server import util


async def get_chromosome_by_assembly_using_get(request: web.Request, chromosome, map_key) -> web.Response:
    """Return a list of chromosomes

    

    :param chromosome: chromosome
    :type chromosome: str
    :param map_key: mapKey
    :type map_key: int

    """
    return web.Response(status=200)


async def get_chromosomes_by_assembly_using_get(request: web.Request, map_key) -> web.Response:
    """Return a list of chromosomes

    

    :param map_key: mapKey
    :type map_key: int

    """
    return web.Response(status=200)
