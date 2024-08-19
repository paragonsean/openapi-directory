from typing import List, Dict
from aiohttp import web

from openapi_server.models.webhook_response import WebhookResponse
from openapi_server.models.webhooks_response import WebhooksResponse
from openapi_server.models.webhooks_subscribe_request import WebhooksSubscribeRequest
from openapi_server import util


async def webhooks_fetch_all(request: web.Request, account_id) -> web.Response:
    """Fetch active webhooks

    When messages are acknowledge by carriers, a notification is sent to the specified URL

    :param account_id: Account to apply operations to
    :type account_id: str

    """
    return web.Response(status=200)


async def webhooks_subscribe(request: web.Request, account_id, body) -> web.Response:
    """Subscribe to message events

    When messages are acknowledge by carriers, a notification is sent to the specified URL

    :param account_id: Account to apply operations to
    :type account_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WebhooksSubscribeRequest.from_dict(body)
    return web.Response(status=200)


async def webhooks_unsubscribe(request: web.Request, account_id, url) -> web.Response:
    """Unsubscribe to message events

    Delete subscription for receiving notifications

    :param account_id: Account to apply operations to
    :type account_id: str
    :param url: Account to apply operations to
    :type url: str

    """
    return web.Response(status=200)
