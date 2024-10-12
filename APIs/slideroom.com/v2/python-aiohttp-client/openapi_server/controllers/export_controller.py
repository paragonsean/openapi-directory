from typing import List, Dict
from aiohttp import web

from openapi_server.models.export_result_v2 import ExportResultV2
from openapi_server import util


async def export_get_v2(request: web.Request, token) -> web.Response:
    """Gets the status/result of a requested export.

    

    :param token: 
    :type token: int

    """
    return web.Response(status=200)
