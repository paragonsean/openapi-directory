from typing import List, Dict
from aiohttp import web

from openapi_server.models.event import Event
from openapi_server import util


async def events_id_get(request: web.Request, id) -> web.Response:
    """events_id_get

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)
