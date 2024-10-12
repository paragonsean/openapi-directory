from typing import List, Dict
from aiohttp import web

from openapi_server.models.matching_url_read import MatchingUrlRead
from openapi_server.models.matching_url_write import MatchingUrlWrite
from openapi_server import util


async def get_matching_url_item(request: web.Request, id) -> web.Response:
    """Retrieves a MatchingUrl resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def post_matching_url_collection(request: web.Request, matching_url=None) -> web.Response:
    """Creates a MatchingUrl resource.

    

    :param matching_url: The new MatchingUrl resource
    :type matching_url: dict | bytes

    """
    matching_url = MatchingUrlWrite.from_dict(matching_url)
    return web.Response(status=200)
