from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def downloadable_link_repository_v1_delete_delete(request: web.Request, id) -> web.Response:
    """products/downloadable-links/{id}

    Delete downloadable link

    :param id: 
    :type id: int

    """
    return web.Response(status=200)
