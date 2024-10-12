from typing import List, Dict
from aiohttp import web

from openapi_server.models.frontend_settings import FrontendSettings
from openapi_server import util


async def frontend_settings_get(request: web.Request, ) -> web.Response:
    """Retrieve frontend specific settings

    


    """
    return web.Response(status=200)
