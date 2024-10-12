from typing import List, Dict
from aiohttp import web

from openapi_server.models.strain import Strain
from openapi_server import util


async def get_all_strains_using_get(request: web.Request, ) -> web.Response:
    """Return all active strains in RGD

    


    """
    return web.Response(status=200)


async def get_strain_by_rgd_id_using_get(request: web.Request, rgd_id) -> web.Response:
    """Return a strain by RGD ID

    

    :param rgd_id: RGD ID of the strain
    :type rgd_id: int

    """
    return web.Response(status=200)


async def get_strains_by_position_using_get(request: web.Request, chr, start, stop, map_key) -> web.Response:
    """Return all active strains by position

    

    :param chr: Chromosome
    :type chr: str
    :param start: Start Position
    :type start: int
    :param stop: Stop Position
    :type stop: int
    :param map_key: RGD Map Key (available through lookup service)
    :type map_key: int

    """
    return web.Response(status=200)
