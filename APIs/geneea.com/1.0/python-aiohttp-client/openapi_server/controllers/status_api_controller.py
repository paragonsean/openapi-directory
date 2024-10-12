from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def status(request: web.Request, ) -> web.Response:
    """Gets status of the Interpretor service

    status


    """
    return web.Response(status=200)
