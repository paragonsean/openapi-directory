from typing import List, Dict
from aiohttp import web

from openapi_server.models.shared_color_transformations import SharedColorTransformations
from openapi_server import util


async def shared_colortransformations_get_id(request: web.Request, id) -> web.Response:
    """ColorTransformations: Get by Id

    Get by Id: Use this method to retrieve a ColorTransformations object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
