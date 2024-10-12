from typing import List, Dict
from aiohttp import web

from openapi_server.models.webhooks_registrations_post_request import WebhooksRegistrationsPostRequest
from openapi_server import util


async def webhooks_registrations_get(request: web.Request, ) -> web.Response:
    """Get webhook registrations

    Get webhook registrations


    """
    return web.Response(status=200)


async def webhooks_registrations_id_delete(request: web.Request, id) -> web.Response:
    """Remove a webhook

    Remove a webhook

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def webhooks_registrations_id_get(request: web.Request, id) -> web.Response:
    """Get details of a webhook registration

    Get details of a webhook registration

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def webhooks_registrations_post(request: web.Request, body=None) -> web.Response:
    """Register a webhook

    Register a webhook

    :param body: the content of the request
    :type body: dict | bytes

    """
    body = WebhooksRegistrationsPostRequest.from_dict(body)
    return web.Response(status=200)
