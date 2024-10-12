from typing import List, Dict
from aiohttp import web

from openapi_server.models.slide_color_maps import SlideColorMaps
from openapi_server import util


async def slides_colormaps_get_id(request: web.Request, id) -> web.Response:
    """ColorMaps: Get by Id

    Get by Id: Use this method to retrieve a ColorMaps object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
