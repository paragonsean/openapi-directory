from typing import List, Dict
from aiohttp import web

from openapi_server.models.link_list_result import LinkListResult
from openapi_server.models.link_resource_format import LinkResourceFormat
from openapi_server import util


async def links_create_or_update(request: web.Request, resource_group_name, hub_name, link_name, api_version, subscription_id, parameters) -> web.Response:
    """links_create_or_update

    Creates a link or updates an existing link in the hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param link_name: The name of the link.
    :type link_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the CreateOrUpdate Link operation.
    :type parameters: dict | bytes

    """
    parameters = LinkResourceFormat.from_dict(parameters)
    return web.Response(status=200)


async def links_delete(request: web.Request, resource_group_name, hub_name, link_name, api_version, subscription_id) -> web.Response:
    """links_delete

    Deletes a link in the hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param link_name: The name of the link.
    :type link_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def links_get(request: web.Request, resource_group_name, hub_name, link_name, api_version, subscription_id) -> web.Response:
    """links_get

    Gets a link in the hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param link_name: The name of the link.
    :type link_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def links_list_by_hub(request: web.Request, resource_group_name, hub_name, api_version, subscription_id) -> web.Response:
    """links_list_by_hub

    Gets all the links in the specified hub.

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
