from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.hook_type import HookType
from openapi_server import util


async def list_hook_types(request: web.Request, ) -> web.Response:
    """list_hook_types

    


    """
    return web.Response(status=200)
