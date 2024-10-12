from typing import List, Dict
from aiohttp import web

from openapi_server.models.theme_background_fills import ThemeBackgroundFills
from openapi_server import util


async def themes_backgroundfills_get_id(request: web.Request, id) -> web.Response:
    """BackgroundFills: Get by Id

    Get by Id: Use this method to retrieve a BackgroundFills object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
