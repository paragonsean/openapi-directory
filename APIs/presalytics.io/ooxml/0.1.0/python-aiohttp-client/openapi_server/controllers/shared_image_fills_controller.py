from typing import List, Dict
from aiohttp import web

from openapi_server.models.shared_image_fills import SharedImageFills
from openapi_server import util


async def shared_imagefills_get_id(request: web.Request, id) -> web.Response:
    """ImageFills: Get by Id

    Get by Id: Use this method to retrieve a ImageFills object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
