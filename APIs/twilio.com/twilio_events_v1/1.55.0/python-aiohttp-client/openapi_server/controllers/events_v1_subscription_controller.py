from typing import List, Dict
from aiohttp import web

from openapi_server.models.events_v1_subscription import EventsV1Subscription
from openapi_server.models.list_subscription_response import ListSubscriptionResponse
from openapi_server import util


async def create_subscription(request: web.Request, description, sink_sid, types) -> web.Response:
    """create_subscription

    Create a new Subscription.

    :param description: A human readable description for the Subscription **This value should not contain PII.**
    :type description: str
    :param sink_sid: The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created.
    :type sink_sid: str
    :param types: An array of objects containing the subscribed Event Types
    :type types: List[]

    """
    return web.Response(status=200)


async def delete_subscription(request: web.Request, sid) -> web.Response:
    """delete_subscription

    Delete a specific Subscription.

    :param sid: A 34 character string that uniquely identifies this Subscription.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_subscription(request: web.Request, sid) -> web.Response:
    """fetch_subscription

    Fetch a specific Subscription.

    :param sid: A 34 character string that uniquely identifies this Subscription.
    :type sid: str

    """
    return web.Response(status=200)


async def list_subscription(request: web.Request, sink_sid=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_subscription

    Retrieve a paginated list of Subscriptions belonging to the account used to make the request.

    :param sink_sid: The SID of the sink that the list of Subscriptions should be filtered by.
    :type sink_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_subscription(request: web.Request, sid, description=None, sink_sid=None) -> web.Response:
    """update_subscription

    Update a Subscription.

    :param sid: A 34 character string that uniquely identifies this Subscription.
    :type sid: str
    :param description: A human readable description for the Subscription.
    :type description: str
    :param sink_sid: The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created.
    :type sink_sid: str

    """
    return web.Response(status=200)
