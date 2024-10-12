from typing import List, Dict
from aiohttp import web

from openapi_server.models.tag import Tag
from openapi_server import util


async def get_tag(request: web.Request, word) -> web.Response:
    """Get a specific tag

    

    :param word: The tag to return.
    :type word: str

    """
    return web.Response(status=200)
