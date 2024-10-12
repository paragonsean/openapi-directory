from typing import List, Dict
from aiohttp import web

from openapi_server.models.relationship_link_list_result import RelationshipLinkListResult
from openapi_server.models.relationship_link_resource_format import RelationshipLinkResourceFormat
from openapi_server import util


async def relationship_links_create_or_update(request: web.Request, resource_group_name, hub_name, relationship_link_name, api_version, subscription_id, parameters) -> web.Response:
    """relationship_links_create_or_update

    Creates a relationship link or updates an existing relationship link within a hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param relationship_link_name: The name of the relationship link.
    :type relationship_link_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the CreateOrUpdate relationship link operation.
    :type parameters: dict | bytes

    """
    parameters = RelationshipLinkResourceFormat.from_dict(parameters)
    return web.Response(status=200)


async def relationship_links_delete(request: web.Request, resource_group_name, hub_name, relationship_link_name, api_version, subscription_id) -> web.Response:
    """relationship_links_delete

    Deletes a relationship link within a hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param relationship_link_name: The name of the relationship.
    :type relationship_link_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def relationship_links_get(request: web.Request, resource_group_name, hub_name, relationship_link_name, api_version, subscription_id) -> web.Response:
    """relationship_links_get

    Gets information about the specified relationship Link.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param relationship_link_name: The name of the relationship link.
    :type relationship_link_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def relationship_links_list_by_hub(request: web.Request, resource_group_name, hub_name, api_version, subscription_id) -> web.Response:
    """relationship_links_list_by_hub

    Gets all relationship links in the hub.

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
