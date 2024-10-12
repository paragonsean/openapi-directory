from typing import List, Dict
from aiohttp import web

from openapi_server.models.theme_effect_map import ThemeEffectMap
from openapi_server import util


async def themes_effectmap_get_id(request: web.Request, id) -> web.Response:
    """EffectMap: Get by Id

    Get by Id: Use this method to retrieve a EffectMap object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
