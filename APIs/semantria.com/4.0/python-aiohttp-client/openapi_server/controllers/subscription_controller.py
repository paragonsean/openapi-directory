from typing import List, Dict
from aiohttp import web

from openapi_server.models.subscription import Subscription
from openapi_server import util


async def get_subscription(request: web.Request, content_type) -> web.Response:
    """Retrieve subscription details

    This method retrieves user&#39;s subscription details that consist of the list of allowed features, configured limits and options on Semantria side.

    :param content_type: 
    :type content_type: str

    """
    return web.Response(status=200)
