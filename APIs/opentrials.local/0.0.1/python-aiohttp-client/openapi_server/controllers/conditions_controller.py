from typing import List, Dict
from aiohttp import web

from openapi_server.models.condition import Condition
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def get_condition(request: web.Request, id) -> web.Response:
    """get_condition

    Returns condition details

    :param id: ID of the condition
    :type id: str

    """
    return web.Response(status=200)
