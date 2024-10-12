from typing import List, Dict
from aiohttp import web

from openapi_server.models.theme_custom_colors import ThemeCustomColors
from openapi_server import util


async def themes_customcolors_get_id(request: web.Request, id) -> web.Response:
    """CustomColors: Get by Id

    Get by Id: Use this method to retrieve a CustomColors object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
