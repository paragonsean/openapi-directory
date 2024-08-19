from typing import List, Dict
from aiohttp import web

from openapi_server.models.cart import Cart
from openapi_server import util


async def post_cart(request: web.Request, site_id, body) -> web.Response:
    """Send a cart for the given site

    

    :param site_id: ID site to send the event
    :type site_id: str
    :param body: cart json for the event
    :type body: dict | bytes

    """
    body = Cart.from_dict(body)
    return web.Response(status=200)
