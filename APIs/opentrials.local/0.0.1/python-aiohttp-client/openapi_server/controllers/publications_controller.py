from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.publication import Publication
from openapi_server import util


async def get_publication(request: web.Request, id) -> web.Response:
    """get_publication

    Returns publication details

    :param id: ID of the publication
    :type id: str

    """
    return web.Response(status=200)
