from typing import List, Dict
from aiohttp import web

from openapi_server.models.numbers_v1_porting_port_in_fetch import NumbersV1PortingPortInFetch
from openapi_server import util


async def fetch_porting_port_in_fetch(request: web.Request, port_in_request_sid) -> web.Response:
    """fetch_porting_port_in_fetch

    Fetch a port in request by SID

    :param port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
    :type port_in_request_sid: str

    """
    return web.Response(status=200)
