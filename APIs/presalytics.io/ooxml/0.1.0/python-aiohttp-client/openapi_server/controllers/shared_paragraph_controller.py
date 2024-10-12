from typing import List, Dict
from aiohttp import web

from openapi_server.models.shared_paragraph import SharedParagraph
from openapi_server import util


async def shared_paragraph_get_id(request: web.Request, id) -> web.Response:
    """Paragraph: Get by Id

    Get by Id: Use this method to retrieve a Paragraph object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
