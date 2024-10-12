from typing import List, Dict
from aiohttp import web

from openapi_server.models.shared_effect_attributes import SharedEffectAttributes
from openapi_server import util


async def shared_effectattributes_get_id(request: web.Request, id) -> web.Response:
    """EffectAttributes: Get by Id

    Get by Id: Use this method to retrieve a EffectAttributes object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
