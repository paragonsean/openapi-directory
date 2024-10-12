from typing import List, Dict
from aiohttp import web

from openapi_server.models.shared_text_container import SharedTextContainer
from openapi_server import util


async def shared_textcontainer_get_id(request: web.Request, id) -> web.Response:
    """TextContainer: Get by Id

    Get by Id: Use this method to retrieve a TextContainer object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
