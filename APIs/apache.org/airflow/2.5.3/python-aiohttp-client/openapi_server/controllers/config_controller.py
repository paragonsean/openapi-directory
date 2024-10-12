from typing import List, Dict
from aiohttp import web

from openapi_server.models.config import Config
from openapi_server.models.error import Error
from openapi_server import util


async def get_config(request: web.Request, ) -> web.Response:
    """Get current configuration

    


    """
    return web.Response(status=200)
