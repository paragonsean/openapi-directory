from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.public_subscription_status import PublicSubscriptionStatus
from openapi_server.models.public_subscription_statuses_response import PublicSubscriptionStatusesResponse
from openapi_server.models.public_update_subscription_status_request import PublicUpdateSubscriptionStatusRequest
from openapi_server import util


async def get_communication_preferences_v3_status_email_email_address_get_email_status(request: web.Request, email_address) -> web.Response:
    """Get subscription statuses for a contact

    Returns a list of subscriptions and their status for a given contact.

    :param email_address: 
    :type email_address: str

    """
    return web.Response(status=200)


async def post_communication_preferences_v3_subscribe_subscribe(request: web.Request, body) -> web.Response:
    """Subscribe a contact

    Subscribes a contact to the given subscription type. This API is not valid to use for subscribing a contact at a brand or portal level and will return an error.

    :param body: 
    :type body: dict | bytes

    """
    body = PublicUpdateSubscriptionStatusRequest.from_dict(body)
    return web.Response(status=200)


async def post_communication_preferences_v3_unsubscribe_unsubscribe(request: web.Request, body) -> web.Response:
    """Unsubscribe a contact

    Unsubscribes a contact from the given subscription type. This API is not valid to use for unsubscribing a contact at a brand or portal level and will return an error.

    :param body: 
    :type body: dict | bytes

    """
    body = PublicUpdateSubscriptionStatusRequest.from_dict(body)
    return web.Response(status=200)
