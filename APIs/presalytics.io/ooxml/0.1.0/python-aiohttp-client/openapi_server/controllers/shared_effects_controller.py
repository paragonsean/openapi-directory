from typing import List, Dict
from aiohttp import web

from openapi_server.models.shared_effects import SharedEffects
from openapi_server import util


async def shared_effects_get_id(request: web.Request, id) -> web.Response:
    """Effects: Get by Id

    Get by Id: Use this method to retrieve a Effects object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
