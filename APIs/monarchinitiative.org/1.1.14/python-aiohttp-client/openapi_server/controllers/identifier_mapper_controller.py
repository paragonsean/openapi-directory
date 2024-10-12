from typing import List, Dict
from aiohttp import web

from openapi_server.models.association import Association
from openapi_server import util


async def get_identifier_mapper(request: web.Request, source, target) -> web.Response:
    """TODO maps a list of identifiers from a source to a target

    

    :param source: 
    :type source: str
    :param target: 
    :type target: str

    """
    return web.Response(status=200)
