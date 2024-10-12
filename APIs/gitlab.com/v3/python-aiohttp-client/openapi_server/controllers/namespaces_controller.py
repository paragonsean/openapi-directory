from typing import List, Dict
from aiohttp import web

from openapi_server.models.namespace import Namespace
from openapi_server import util


async def get_v3_namespaces(request: web.Request, search=None, page=None, per_page=None) -> web.Response:
    """Get a namespaces list

    Get a namespaces list

    :param search: Search query for namespaces
    :type search: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)
