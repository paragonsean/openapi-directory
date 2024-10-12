from typing import List, Dict
from aiohttp import web

from openapi_server.models.events_v1_subscription_subscribed_event import EventsV1SubscriptionSubscribedEvent
from openapi_server.models.list_subscribed_event_response import ListSubscribedEventResponse
from openapi_server import util


async def create_subscribed_event(request: web.Request, subscription_sid, type, schema_version=None) -> web.Response:
    """create_subscribed_event

    Add an event type to a Subscription.

    :param subscription_sid: The unique SID identifier of the Subscription.
    :type subscription_sid: str
    :param type: Type of event being subscribed to.
    :type type: str
    :param schema_version: The schema version that the Subscription should use.
    :type schema_version: int

    """
    return web.Response(status=200)


async def delete_subscribed_event(request: web.Request, subscription_sid, type) -> web.Response:
    """delete_subscribed_event

    Remove an event type from a Subscription.

    :param subscription_sid: The unique SID identifier of the Subscription.
    :type subscription_sid: str
    :param type: Type of event being subscribed to.
    :type type: str

    """
    return web.Response(status=200)


async def fetch_subscribed_event(request: web.Request, subscription_sid, type) -> web.Response:
    """fetch_subscribed_event

    Read an Event for a Subscription.

    :param subscription_sid: The unique SID identifier of the Subscription.
    :type subscription_sid: str
    :param type: Type of event being subscribed to.
    :type type: str

    """
    return web.Response(status=200)


async def list_subscribed_event(request: web.Request, subscription_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_subscribed_event

    Retrieve a list of all Subscribed Event types for a Subscription.

    :param subscription_sid: The unique SID identifier of the Subscription.
    :type subscription_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_subscribed_event(request: web.Request, subscription_sid, type, schema_version=None) -> web.Response:
    """update_subscribed_event

    Update an Event for a Subscription.

    :param subscription_sid: The unique SID identifier of the Subscription.
    :type subscription_sid: str
    :param type: Type of event being subscribed to.
    :type type: str
    :param schema_version: The schema version that the Subscription should use.
    :type schema_version: int

    """
    return web.Response(status=200)
