from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response_content import ErrorResponseContent
from openapi_server.models.webhook_base_info import WebhookBaseInfo
from openapi_server.models.webhook_info import WebhookInfo
from openapi_server import util


async def get_webhook_by_id(request: web.Request, webhook_id) -> web.Response:
    """Get Webhook by Id

    Returns information of the webhook specified by the passed id.

    :param webhook_id: Id of the outbound webhook to be retrieved.
    :type webhook_id: str

    """
    return web.Response(status=200)


async def webhooks_get(request: web.Request, team_id=None) -> web.Response:
    """Get Webhooks

    Returns a collection of defined outbound webhooks in the system.

    :param team_id: 
    :type team_id: str

    """
    return web.Response(status=200)


async def webhooks_post(request: web.Request, body=None) -> web.Response:
    """Create Webhook

    Creates a new outbound webhook that will be notified when certain events occur.

    :param body: Json object that contains the external URL of the webhook.
    :type body: dict | bytes

    """
    body = WebhookBaseInfo.from_dict(body)
    return web.Response(status=200)


async def webhooks_webhook_id_delete(request: web.Request, webhook_id) -> web.Response:
    """Delete Webhook by Id

    Deletes the specified webhook so that it will no longer be notified.

    :param webhook_id: Id of the outbound webhook that will be deleted.
    :type webhook_id: str

    """
    return web.Response(status=200)


async def webhooks_webhook_id_disable_post(request: web.Request, webhook_id) -> web.Response:
    """Ability to enable a webHook.

    

    :param webhook_id: Webhook ID for webhook which should be disabled.
    :type webhook_id: str

    """
    return web.Response(status=200)


async def webhooks_webhook_id_enable_post(request: web.Request, webhook_id) -> web.Response:
    """Ability to disable a webHook.

    

    :param webhook_id: Webhook ID for webhook which should be enabled.
    :type webhook_id: str

    """
    return web.Response(status=200)


async def webhooks_webhook_id_put(request: web.Request, webhook_id, body=None) -> web.Response:
    """Update Webhook by Id

    Updates the specified webhook.

    :param webhook_id: Id of the outbound webhook to be updated.
    :type webhook_id: str
    :param body: Json object containing the updated URL of the webhook.
    :type body: dict | bytes

    """
    body = WebhookBaseInfo.from_dict(body)
    return web.Response(status=200)
