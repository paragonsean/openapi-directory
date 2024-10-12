from typing import List, Dict
from aiohttp import web

from openapi_server.models.content_rating import ContentRating
from openapi_server import util


async def get_content_ratings(request: web.Request, ) -> web.Response:
    """Get all content ratings

    


    """
    return web.Response(status=200)
