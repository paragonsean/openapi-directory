from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.organisation import Organisation
from openapi_server import util


async def get_organisation(request: web.Request, id) -> web.Response:
    """get_organisation

    Returns organisation details

    :param id: ID of the organisation
    :type id: str

    """
    return web.Response(status=200)
