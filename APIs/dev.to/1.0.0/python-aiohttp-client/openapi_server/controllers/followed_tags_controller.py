from typing import List, Dict
from aiohttp import web

from openapi_server.models.followed_tag import FollowedTag
from openapi_server import util


async def get_followed_tags(request: web.Request, ) -> web.Response:
    """Followed Tags

    This endpoint allows the client to retrieve a list of the tags they follow.


    """
    return web.Response(status=200)
