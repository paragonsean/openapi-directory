from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_webhook_request import CreateWebhookRequest
from openapi_server.models.create_webhook_response import CreateWebhookResponse
from openapi_server.models.delete_webhook_response import DeleteWebhookResponse
from openapi_server.models.get_webhook_event_logs_response import GetWebhookEventLogsResponse
from openapi_server.models.get_webhook_response import GetWebhookResponse
from openapi_server.models.get_webhooks_response import GetWebhooksResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_webhook_request import UpdateWebhookRequest
from openapi_server.models.update_webhook_response import UpdateWebhookResponse
from openapi_server.models.webhook_event_logs_filter import WebhookEventLogsFilter
from openapi_server import util


async def event_logs_all(request: web.Request, x_apideck_app_id, cursor=None, limit=None, filter=None) -> web.Response:
    """List event logs

    List event logs

    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param cursor: Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    :type cursor: str
    :param limit: Number of results to return. Minimum 1, Maximum 200, Default 20
    :type limit: int
    :param filter: Filter results
    :type filter: dict | bytes

    """
    filter = .from_dict(filter)
    return web.Response(status=200)


async def webhooks_add(request: web.Request, x_apideck_app_id, body) -> web.Response:
    """Create webhook subscription

    Create a webhook subscription to receive events

    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateWebhookRequest.from_dict(body)
    return web.Response(status=200)


async def webhooks_all(request: web.Request, x_apideck_app_id, cursor=None, limit=None) -> web.Response:
    """List webhook subscriptions

    List all webhook subscriptions

    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param cursor: Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    :type cursor: str
    :param limit: Number of results to return. Minimum 1, Maximum 200, Default 20
    :type limit: int

    """
    return web.Response(status=200)


async def webhooks_delete(request: web.Request, id, x_apideck_app_id) -> web.Response:
    """Delete webhook subscription

    Delete a webhook subscription

    :param id: JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.
    :type id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str

    """
    return web.Response(status=200)


async def webhooks_one(request: web.Request, id, x_apideck_app_id) -> web.Response:
    """Get webhook subscription

    Get the webhook subscription details

    :param id: JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.
    :type id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str

    """
    return web.Response(status=200)


async def webhooks_update(request: web.Request, id, x_apideck_app_id, body) -> web.Response:
    """Update webhook subscription

    Update a webhook subscription

    :param id: JWT Webhook token that represents the unifiedApi and applicationId associated to the event source.
    :type id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateWebhookRequest.from_dict(body)
    return web.Response(status=200)
