from typing import List, Dict
from aiohttp import web

from openapi_server.models.slide_group_elements import SlideGroupElements
from openapi_server import util


async def slides_groupelements_get_id(request: web.Request, id) -> web.Response:
    """GroupElements: Get by Id

    Get by Id: Use this method to retrieve a GroupElements object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
