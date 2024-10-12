from typing import List, Dict
from aiohttp import web

from openapi_server.models.slide_graphics import SlideGraphics
from openapi_server import util


async def slides_graphics_get_id(request: web.Request, id) -> web.Response:
    """Graphics: Get by Id

    Get by Id: Use this method to retrieve a Graphics object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
