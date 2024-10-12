from typing import List, Dict
from aiohttp import web

from openapi_server.models.association import Association
from openapi_server import util


async def get_dl_query(request: web.Request, query) -> web.Response:
    """Placeholder - use OWLery for now

    

    :param query: 
    :type query: str

    """
    return web.Response(status=200)


async def get_sparql_query(request: web.Request, query) -> web.Response:
    """Placeholder - use direct SPARQL endpoint for now

    

    :param query: 
    :type query: str

    """
    return web.Response(status=200)
