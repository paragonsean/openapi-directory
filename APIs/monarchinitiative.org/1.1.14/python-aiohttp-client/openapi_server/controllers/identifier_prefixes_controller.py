from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_prefix_collection(request: web.Request, ) -> web.Response:
    """Returns list of prefixes

    


    """
    return web.Response(status=200)


async def get_prefix_contract(request: web.Request, uri) -> web.Response:
    """Returns contracted URI

    

    :param uri: URI of entity to be contracted to identifier/CURIE, e.g \&quot;http://www.informatics.jax.org/accession/MGI:1\&quot;
    :type uri: str

    """
    return web.Response(status=200)


async def get_prefix_expand(request: web.Request, id) -> web.Response:
    """Returns expanded URI

    

    :param id: ID of entity to be contracted to URI, e.g \&quot;MGI:1\&quot;
    :type id: str

    """
    return web.Response(status=200)
