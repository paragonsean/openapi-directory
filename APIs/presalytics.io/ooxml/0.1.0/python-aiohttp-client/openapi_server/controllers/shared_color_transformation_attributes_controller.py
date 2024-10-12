from typing import List, Dict
from aiohttp import web

from openapi_server.models.shared_color_transformation_attributes import SharedColorTransformationAttributes
from openapi_server import util


async def shared_colortransformationattributes_get_id(request: web.Request, id) -> web.Response:
    """ColorTransformationAttributes: Get by Id

    Get by Id: Use this method to retrieve a ColorTransformationAttributes object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
