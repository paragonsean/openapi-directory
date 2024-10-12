from typing import List, Dict
from aiohttp import web

from openapi_server.models.theme_line_map import ThemeLineMap
from openapi_server import util


async def themes_linemap_get_id(request: web.Request, id) -> web.Response:
    """LineMap: Get by Id

    Get by Id: Use this method to retrieve a LineMap object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
