from typing import List, Dict
from aiohttp import web

from openapi_server.models.hub import Hub
from openapi_server.models.hub_list_result import HubListResult
from openapi_server import util


async def hubs_create_or_update(request: web.Request, resource_group_name, hub_name, api_version, subscription_id, parameters) -> web.Response:
    """hubs_create_or_update

    Creates a hub, or updates an existing hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the Hub.
    :type hub_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the CreateOrUpdate Hub operation.
    :type parameters: dict | bytes

    """
    parameters = Hub.from_dict(parameters)
    return web.Response(status=200)


async def hubs_delete(request: web.Request, resource_group_name, hub_name, api_version, subscription_id) -> web.Response:
    """hubs_delete

    Deletes the specified hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def hubs_get(request: web.Request, resource_group_name, hub_name, api_version, subscription_id) -> web.Response:
    """hubs_get

    Gets information about the specified hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def hubs_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """hubs_list

    Gets all hubs in the specified subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def hubs_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """hubs_list_by_resource_group

    Gets all the hubs in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def hubs_update(request: web.Request, resource_group_name, hub_name, api_version, subscription_id, parameters) -> web.Response:
    """hubs_update

    Updates a Hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the Hub.
    :type hub_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Update Hub operation.
    :type parameters: dict | bytes

    """
    parameters = Hub.from_dict(parameters)
    return web.Response(status=200)
