from typing import List, Dict
from aiohttp import web

from openapi_server.models.shared_lines import SharedLines
from openapi_server import util


async def shared_lines_get_id(request: web.Request, id) -> web.Response:
    """Lines: Get by Id

    Get by Id: Use this method to retrieve a Lines object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
