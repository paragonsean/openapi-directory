from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_a_webhook_request import CreateAWebhookRequest
from openapi_server import util


async def create_a_webhook(request: web.Request, org_id, body=None) -> web.Response:
    """Create a webhook

    

    :param org_id: The organization ID to list projects for. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateAWebhookRequest.from_dict(body)
    return web.Response(status=200)


async def delete_a_webhook(request: web.Request, org_id, webhook_id) -> web.Response:
    """Delete a webhook

    

    :param org_id: Automatically added
    :type org_id: str
    :param webhook_id: Automatically added
    :type webhook_id: str

    """
    return web.Response(status=200)


async def list_webhooks(request: web.Request, org_id) -> web.Response:
    """List webhooks

    

    :param org_id: The organization ID to list projects for. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str

    """
    return web.Response(status=200)


async def ping_a_webhook(request: web.Request, org_id, webhook_id) -> web.Response:
    """Ping a webhook

    

    :param org_id: The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param webhook_id: The webhook ID.
    :type webhook_id: str

    """
    return web.Response(status=200)


async def retrieve_a_webhook(request: web.Request, org_id, webhook_id) -> web.Response:
    """Retrieve a webhook

    

    :param org_id: The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param webhook_id: The webhook ID.
    :type webhook_id: str

    """
    return web.Response(status=200)
