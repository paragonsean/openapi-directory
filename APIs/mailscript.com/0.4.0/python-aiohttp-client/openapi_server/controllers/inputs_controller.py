from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_all_inputs_response import GetAllInputsResponse
from openapi_server import util


async def get_all_inputs(request: web.Request, name=None) -> web.Response:
    """Get all inputs you have access to

    

    :param name: 
    :type name: str

    """
    return web.Response(status=200)
