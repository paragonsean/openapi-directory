from typing import List, Dict
from aiohttp import web

from openapi_server.models.shared_solid_fills import SharedSolidFills
from openapi_server import util


async def shared_solidfills_get_id(request: web.Request, id) -> web.Response:
    """SolidFills: Get by Id

    Get by Id: Use this method to retrieve a SolidFills object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
