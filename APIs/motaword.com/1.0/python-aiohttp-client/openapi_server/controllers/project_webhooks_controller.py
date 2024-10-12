from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.project import Project
from openapi_server.models.webhook import Webhook
from openapi_server import util


async def delete_project_webhook(request: web.Request, id) -> web.Response:
    """Delete project webhooks

    Delete project webhooks. Projects currently support registering only 1 webhook. This endpoint deletes the previously registered webhook.

    :param id: Project ID
    :type id: int

    """
    return web.Response(status=200)


async def get_project_webhooks(request: web.Request, id) -> web.Response:
    """View project webhooks

    This endpoint returns Project entity which contains &#x60;callback_url&#x60; field for webhook URL. Currently projects can have only 1 webhook registered.

    :param id: Project ID
    :type id: int

    """
    return web.Response(status=200)


async def post_project_webhook(request: web.Request, id, body=None) -> web.Response:
    """Update project webhook

    Update project webhook URL

    :param id: Project ID
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Webhook.from_dict(body)
    return web.Response(status=200)


async def update_project_webhook(request: web.Request, id, body=None) -> web.Response:
    """Update project webhook

    Update project webhook URL

    :param id: Project ID
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Webhook.from_dict(body)
    return web.Response(status=200)
