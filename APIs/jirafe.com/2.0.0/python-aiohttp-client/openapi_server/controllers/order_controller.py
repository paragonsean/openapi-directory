from typing import List, Dict
from aiohttp import web

from openapi_server.models.order_cancelled import OrderCancelled
from openapi_server import util


async def post_order_cancelled(request: web.Request, site_id, body) -> web.Response:
    """Send a order for the given site

    

    :param site_id: ID site to send the event
    :type site_id: str
    :param body: order json for the event
    :type body: dict | bytes

    """
    body = OrderCancelled.from_dict(body)
    return web.Response(status=200)
