from typing import List, Dict
from aiohttp import web

from openapi_server.models.category import Category
from openapi_server import util


async def post_category(request: web.Request, site_id, body) -> web.Response:
    """Send a category for the given site

    

    :param site_id: ID site to send the event
    :type site_id: str
    :param body: category json for the event
    :type body: dict | bytes

    """
    body = Category.from_dict(body)
    return web.Response(status=200)
