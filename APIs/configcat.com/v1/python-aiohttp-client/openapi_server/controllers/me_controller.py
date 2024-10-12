from typing import List, Dict
from aiohttp import web

from openapi_server.models.me_model import MeModel
from openapi_server import util


async def get_me(request: web.Request, ) -> web.Response:
    """Get authenticated user details

    


    """
    return web.Response(status=200)
