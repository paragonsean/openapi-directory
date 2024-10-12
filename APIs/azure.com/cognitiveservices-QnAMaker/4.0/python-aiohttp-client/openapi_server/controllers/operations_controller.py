from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.operation import Operation
from openapi_server import util


async def operations_get_details(request: web.Request, operation_id) -> web.Response:
    """Gets details of a specific long running operation.

    

    :param operation_id: Operation id.
    :type operation_id: str

    """
    return web.Response(status=200)
