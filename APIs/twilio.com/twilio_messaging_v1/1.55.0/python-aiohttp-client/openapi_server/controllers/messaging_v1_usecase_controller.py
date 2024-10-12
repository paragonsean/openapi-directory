from typing import List, Dict
from aiohttp import web

from openapi_server.models.messaging_v1_usecase import MessagingV1Usecase
from openapi_server import util


async def fetch_usecase(request: web.Request, ) -> web.Response:
    """fetch_usecase

    


    """
    return web.Response(status=200)
