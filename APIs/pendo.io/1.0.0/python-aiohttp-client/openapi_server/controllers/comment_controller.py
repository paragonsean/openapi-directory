from typing import List, Dict
from aiohttp import web

from openapi_server.models.comment import Comment
from openapi_server import util


async def comments_get(request: web.Request, case_id) -> web.Response:
    """fetch Comment records

    get a list of Comment records

    :param case_id: case_id
    :type case_id: int

    """
    return web.Response(status=200)
