from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_webhook_request_body import CreateWebhookRequestBody
from openapi_server.models.create_webhook_response_body import CreateWebhookResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_webhook_by_id_response_body import GetWebhookByIdResponseBody
from openapi_server.models.update_webhook_request_body import UpdateWebhookRequestBody
from openapi_server.models.webhook import Webhook
from openapi_server import util


async def create_webhook(request: web.Request, body) -> web.Response:
    """Create a Webhook

    Create a webook for specific events in the environment.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateWebhookRequestBody.from_dict(body)
    return web.Response(status=200)


async def delete_webhook(request: web.Request, webhook_id) -> web.Response:
    """Delete Webhook By ID

    Delete a webhook

    :param webhook_id: Webhook ID
    :type webhook_id: str

    """
    return web.Response(status=200)


async def get_webhook_by_id(request: web.Request, webhook_id) -> web.Response:
    """Get Webhook By ID

    Retrieve individual webhook by an ID

    :param webhook_id: Webhook ID
    :type webhook_id: str

    """
    return web.Response(status=200)


async def list_webhooks(request: web.Request, ) -> web.Response:
    """List Webhooks

    List all webhooks currently enabled for the account.


    """
    return web.Response(status=200)


async def update_webhook(request: web.Request, webhook_id, body) -> web.Response:
    """Update a Webhook

    Update the webhook url property

    :param webhook_id: Webhook ID
    :type webhook_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateWebhookRequestBody.from_dict(body)
    return web.Response(status=200)
