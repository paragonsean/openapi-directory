from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer import Customer
from openapi_server import util


async def post_customer(request: web.Request, site_id, body) -> web.Response:
    """Send a customer for the given site

    

    :param site_id: ID site to send the event
    :type site_id: str
    :param body: customer json for the event
    :type body: dict | bytes

    """
    body = Customer.from_dict(body)
    return web.Response(status=200)
