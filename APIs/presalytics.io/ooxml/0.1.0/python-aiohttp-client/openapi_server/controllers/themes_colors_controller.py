from typing import List, Dict
from aiohttp import web

from openapi_server.models.theme_colors import ThemeColors
from openapi_server import util


async def themes_colors_get_id(request: web.Request, id) -> web.Response:
    """Colors: Get by Id

    Get by Id: Use this method to retrieve a Colors object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
