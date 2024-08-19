from typing import List, Dict
from aiohttp import web

from openapi_server.models.client_error_response import ClientErrorResponse
from openapi_server.models.id import Id
from openapi_server.models.server_error_response import ServerErrorResponse
from openapi_server.models.validation_error_response import ValidationErrorResponse
from openapi_server import util


async def get_id(request: web.Request, id) -> web.Response:
    """Convert legacy ID to v3 ID.

    Retrieves the API v3 ID.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)
