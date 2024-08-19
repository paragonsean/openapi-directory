from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_webhook_feed_data_request import CreateWebhookFeedDataRequest
from openapi_server.models.data import Data
from openapi_server import util


async def create_raw_webhook_feed_data(request: web.Request, ) -> web.Response:
    """Send arbitrary data to a feed via webhook URL.

    The raw data webhook receiver accepts POST requests and stores the raw request body on your feed. This is useful when you don&#39;t have control of the webhook sender. If feed history is turned on, payloads will be truncated at 1024 bytes. If feed history is turned off, payloads will be truncated at 100KB.


    """
    return web.Response(status=200)


async def create_webhook_feed_data(request: web.Request, payload) -> web.Response:
    """Send data to a feed via webhook URL.

    

    :param payload: Webhook payload containing data &#x60;value&#x60; parameter.
    :type payload: dict | bytes

    """
    payload = CreateWebhookFeedDataRequest.from_dict(payload)
    return web.Response(status=200)
