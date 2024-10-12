from typing import List, Dict
from aiohttp import web

from openapi_server.models.shared_gradient_fills import SharedGradientFills
from openapi_server import util


async def shared_gradientfills_get_id(request: web.Request, id) -> web.Response:
    """GradientFills: Get by Id

    Get by Id: Use this method to retrieve a GradientFills object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
