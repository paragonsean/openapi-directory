from typing import List, Dict
from aiohttp import web

from openapi_server.models.webhook import Webhook
from openapi_server import util


async def setup_webhook_get(request: web.Request, ) -> web.Response:
    """Returns a list of webhooks

    Returns a list of webhooks you&#39;ve previously created. The webhooks are returned in sorted order, with the most recent webhook appearing first.


    """
    return web.Response(status=200)


async def setup_webhook_id_delete(request: web.Request, id) -> web.Response:
    """Delete a webhook

    Deletes the specified webhook.

    :param id: Webhook ID.
    :type id: str

    """
    return web.Response(status=200)


async def setup_webhook_id_get(request: web.Request, id) -> web.Response:
    """Retrieve an existing webhook

    Retrieves the details of an existing webhook. You need only supply the unique webhook identifier that was returned upon webhook creation.

    :param id: Webhook ID.
    :type id: str

    """
    return web.Response(status=200)


async def setup_webhook_post(request: web.Request, ) -> web.Response:
    """Create or update a webhook

    Creates or updates the specified webhook. Any parameters not provided will be left unchanged.


    """
    return web.Response(status=200)
