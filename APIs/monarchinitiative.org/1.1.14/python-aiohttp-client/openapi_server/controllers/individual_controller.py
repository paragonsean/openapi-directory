from typing import List, Dict
from aiohttp import web

from openapi_server.models.association import Association
from openapi_server import util


async def get_individual(request: web.Request, id) -> web.Response:
    """Returns list of matches

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_pedigree(request: web.Request, id) -> web.Response:
    """Returns list of matches

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
