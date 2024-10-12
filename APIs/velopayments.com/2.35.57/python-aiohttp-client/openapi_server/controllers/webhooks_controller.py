from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_webhook_request import CreateWebhookRequest
from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server.models.ping_response import PingResponse
from openapi_server.models.update_webhook_request import UpdateWebhookRequest
from openapi_server.models.webhook_response import WebhookResponse
from openapi_server.models.webhooks_response import WebhooksResponse
from openapi_server import util


async def create_webhook_v1(request: web.Request, body=None) -> web.Response:
    """Create Webhook

    Create Webhook

    :param body: 
    :type body: dict | bytes

    """
    body = CreateWebhookRequest.from_dict(body)
    return web.Response(status=200)


async def get_webhook_v1(request: web.Request, webhook_id) -> web.Response:
    """Get details about the given webhook.

    Get details about the given webhook.

    :param webhook_id: Webhook id
    :type webhook_id: str
    :type webhook_id: str

    """
    return web.Response(status=200)


async def list_webhooks_v1(request: web.Request, payor_id, page=None, page_size=None) -> web.Response:
    """List the details about the webhooks for the given payor.

    List the details about the webhooks for the given payor.

    :param payor_id: The Payor ID
    :type payor_id: str
    :type payor_id: str
    :param page: Page number. Default is 1.
    :type page: int
    :param page_size: The number of results to return in a page
    :type page_size: int

    """
    return web.Response(status=200)


async def ping_webhook_v1(request: web.Request, webhook_id) -> web.Response:
    """ping_webhook_v1

    

    :param webhook_id: Webhook id
    :type webhook_id: str
    :type webhook_id: str

    """
    return web.Response(status=200)


async def update_webhook_v1(request: web.Request, webhook_id, body=None) -> web.Response:
    """Update Webhook

    Update Webhook

    :param webhook_id: Webhook id
    :type webhook_id: str
    :type webhook_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateWebhookRequest.from_dict(body)
    return web.Response(status=200)
