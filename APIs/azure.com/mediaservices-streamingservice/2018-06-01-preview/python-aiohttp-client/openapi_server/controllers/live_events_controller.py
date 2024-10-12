from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.live_event import LiveEvent
from openapi_server.models.live_event_action_input import LiveEventActionInput
from openapi_server.models.live_event_list_result import LiveEventListResult
from openapi_server import util


async def live_events_create(request: web.Request, subscription_id, resource_group_name, account_name, live_event_name, api_version, parameters, auto_start=None) -> web.Response:
    """Create Live Event

    Creates a Live Event.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param live_event_name: The name of the Live Event.
    :type live_event_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: Live Event properties needed for creation.
    :type parameters: dict | bytes
    :param auto_start: The flag indicates if auto start the Live Event.
    :type auto_start: bool

    """
    parameters = LiveEvent.from_dict(parameters)
    return web.Response(status=200)


async def live_events_delete(request: web.Request, subscription_id, resource_group_name, account_name, live_event_name, api_version) -> web.Response:
    """Delete Live Event

    Deletes a Live Event.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param live_event_name: The name of the Live Event.
    :type live_event_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def live_events_get(request: web.Request, subscription_id, resource_group_name, account_name, live_event_name, api_version) -> web.Response:
    """Get Live Event

    Gets a Live Event.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param live_event_name: The name of the Live Event.
    :type live_event_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def live_events_list(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """List Live Events

    Lists the Live Events in the account.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def live_events_reset(request: web.Request, subscription_id, resource_group_name, account_name, live_event_name, api_version) -> web.Response:
    """Reset Live Event

    Resets an existing Live Event.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param live_event_name: The name of the Live Event.
    :type live_event_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def live_events_start(request: web.Request, subscription_id, resource_group_name, account_name, live_event_name, api_version) -> web.Response:
    """Start Live Event

    Starts an existing Live Event.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param live_event_name: The name of the Live Event.
    :type live_event_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def live_events_stop(request: web.Request, subscription_id, resource_group_name, account_name, live_event_name, api_version, parameters) -> web.Response:
    """Stop Live Event

    Stops an existing Live Event.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param live_event_name: The name of the Live Event.
    :type live_event_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: LiveEvent stop parameters
    :type parameters: dict | bytes

    """
    parameters = LiveEventActionInput.from_dict(parameters)
    return web.Response(status=200)


async def live_events_update(request: web.Request, subscription_id, resource_group_name, account_name, live_event_name, api_version, parameters) -> web.Response:
    """live_events_update

    Updates a existing Live Event.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param live_event_name: The name of the Live Event.
    :type live_event_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: Live Event properties needed for creation.
    :type parameters: dict | bytes

    """
    parameters = LiveEvent.from_dict(parameters)
    return web.Response(status=200)
