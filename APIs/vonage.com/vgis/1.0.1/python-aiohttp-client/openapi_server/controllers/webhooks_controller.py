from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.webhook import Webhook
from openapi_server.models.webhook_create import WebhookCreate
from openapi_server import util


async def create_webhook(request: web.Request, body) -> web.Response:
    """Create a new webhook subscription

    

    :param body: Webhook create parameters
    :type body: dict | bytes

    """
    body = WebhookCreate.from_dict(body)
    return web.Response(status=200)


async def destroy_webhook(request: web.Request, id) -> web.Response:
    """Remove a web hook

    

    :param id: Unique identifier of the webhook
    :type id: str

    """
    return web.Response(status=200)


async def list_webhooks(request: web.Request, ) -> web.Response:
    """List web hooks

    


    """
    return web.Response(status=200)


async def renew_webhook(request: web.Request, id) -> web.Response:
    """Renews a web hook

    

    :param id: Webhook ID
    :type id: str

    """
    return web.Response(status=200)


async def view_webhook(request: web.Request, id) -> web.Response:
    """Get web hook details

    

    :param id: Unique identifier of the webhook
    :type id: str

    """
    return web.Response(status=200)
