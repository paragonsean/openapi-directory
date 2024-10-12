from typing import List, Dict
from aiohttp import web

from openapi_server.models.connection_id_request_body import ConnectionIdRequestBody
from openapi_server.models.connection_state import ConnectionState
from openapi_server.models.connection_state_create_or_update import ConnectionStateCreateOrUpdate
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server import util


async def create_or_update_state(request: web.Request, body) -> web.Response:
    """Create or update the state for a connection.

    

    :param body: 
    :type body: dict | bytes

    """
    body = ConnectionStateCreateOrUpdate.from_dict(body)
    return web.Response(status=200)


async def get_state(request: web.Request, body) -> web.Response:
    """Fetch the current state for a connection.

    

    :param body: 
    :type body: dict | bytes

    """
    body = ConnectionIdRequestBody.from_dict(body)
    return web.Response(status=200)
