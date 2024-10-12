from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def docket(request: web.Request, response_format, docket_id) -> web.Response:
    """Returns Docket information

    

    :param response_format: Format
    :type response_format: str
    :param docket_id: Docket ID
    :type docket_id: str

    """
    return web.Response(status=200)
