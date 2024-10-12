from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.system_status_response_schema import SystemStatusResponseSchema
from openapi_server import util


async def systemstatus_get(request: web.Request, ) -> web.Response:
    """systemstatus_get

    Returns the overall system status of the Mastercard Digital Enablement Service.


    """
    return web.Response(status=200)
