from typing import List, Dict
from aiohttp import web

from openapi_server.models.live_events_list_default_response import LiveEventsListDefaultResponse
from openapi_server.models.live_output import LiveOutput
from openapi_server.models.live_output_list_result import LiveOutputListResult
from openapi_server import util


async def live_outputs_create(request: web.Request, subscription_id, resource_group_name, account_name, live_event_name, live_output_name, api_version, parameters) -> web.Response:
    """Create Live Output

    Creates a Live Output.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param live_event_name: The name of the Live Event.
    :type live_event_name: str
    :param live_output_name: The name of the Live Output.
    :type live_output_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: Live Output properties needed for creation.
    :type parameters: dict | bytes

    """
    parameters = LiveOutput.from_dict(parameters)
    return web.Response(status=200)


async def live_outputs_delete(request: web.Request, subscription_id, resource_group_name, account_name, live_event_name, live_output_name, api_version) -> web.Response:
    """Delete Live Output

    Deletes a Live Output.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param live_event_name: The name of the Live Event.
    :type live_event_name: str
    :param live_output_name: The name of the Live Output.
    :type live_output_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def live_outputs_get(request: web.Request, subscription_id, resource_group_name, account_name, live_event_name, live_output_name, api_version) -> web.Response:
    """Get Live Output

    Gets a Live Output.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param live_event_name: The name of the Live Event.
    :type live_event_name: str
    :param live_output_name: The name of the Live Output.
    :type live_output_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def live_outputs_list(request: web.Request, subscription_id, resource_group_name, account_name, live_event_name, api_version) -> web.Response:
    """List Live Outputs

    Lists the Live Outputs in the Live Event.

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
