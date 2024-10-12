from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.ping_response import PingResponse
from openapi_server import util


async def util_ping_get(request: web.Request, ) -> web.Response:
    """Ping

    Make a basic ping request to the API. This is useful to verify that authentication is functioning correctly. On authentication success an HTTP &#x60;200&#x60; status is returned. On failure an HTTP &#x60;401&#x60; error response is returned. 


    """
    return web.Response(status=200)
