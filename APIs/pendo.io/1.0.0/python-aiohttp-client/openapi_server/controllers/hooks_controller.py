from typing import List, Dict
from aiohttp import web

from openapi_server.models.hooks_post_request import HooksPostRequest
from openapi_server.models.hooks_unsubscribe_post_request import HooksUnsubscribePostRequest
from openapi_server import util


async def hooks_post(request: web.Request, data) -> web.Response:
    """Subscribe to webhooks

    Use this endpoint to subscribe to webhooks.

    :param data: 
    :type data: dict | bytes

    """
    data = HooksPostRequest.from_dict(data)
    return web.Response(status=200)


async def hooks_unsubscribe_post(request: web.Request, data) -> web.Response:
    """Unsubscribe from webhooks

    Use this endpoint to unsubscribe from a webhook

    :param data: 
    :type data: dict | bytes

    """
    data = HooksUnsubscribePostRequest.from_dict(data)
    return web.Response(status=200)
