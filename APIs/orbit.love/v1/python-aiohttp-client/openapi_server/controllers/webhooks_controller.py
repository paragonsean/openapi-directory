from typing import List, Dict
from aiohttp import web

from openapi_server.models.webhook_subscription import WebhookSubscription
from openapi_server import util


async def workspace_slug_webhooks_get(request: web.Request, workspace_slug) -> web.Response:
    """List webhooks in a workspace

    

    :param workspace_slug: 
    :type workspace_slug: str

    """
    return web.Response(status=200)


async def workspace_slug_webhooks_id_delete(request: web.Request, workspace_slug, id) -> web.Response:
    """Delete a webhook

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def workspace_slug_webhooks_id_get(request: web.Request, workspace_slug, id) -> web.Response:
    """Get a webhook

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def workspace_slug_webhooks_id_put(request: web.Request, workspace_slug, id, body=None) -> web.Response:
    """Update a webhook

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WebhookSubscription.from_dict(body)
    return web.Response(status=200)


async def workspace_slug_webhooks_post(request: web.Request, workspace_slug, body=None) -> web.Response:
    """Create a webhook

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = WebhookSubscription.from_dict(body)
    return web.Response(status=200)
