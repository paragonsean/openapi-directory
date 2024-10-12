from typing import List, Dict
from aiohttp import web

from openapi_server.models.otoroshi_health import OtoroshiHealth
from openapi_server import util


async def health(request: web.Request, ) -> web.Response:
    """Return current Otoroshi health

    Import the full state of Otoroshi as a file


    """
    return web.Response(status=200)
