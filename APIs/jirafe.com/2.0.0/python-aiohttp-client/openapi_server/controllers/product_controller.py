from typing import List, Dict
from aiohttp import web

from openapi_server.models.product import Product
from openapi_server import util


async def post_product(request: web.Request, site_id, body) -> web.Response:
    """Send a product for the given site

    

    :param site_id: ID site to send the event
    :type site_id: str
    :param body: product json for the event
    :type body: dict | bytes

    """
    body = Product.from_dict(body)
    return web.Response(status=200)
