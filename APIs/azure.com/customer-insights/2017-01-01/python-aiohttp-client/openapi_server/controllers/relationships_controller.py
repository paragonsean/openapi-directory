from typing import List, Dict
from aiohttp import web

from openapi_server.models.relationship_list_result import RelationshipListResult
from openapi_server.models.relationship_resource_format import RelationshipResourceFormat
from openapi_server import util


async def relationships_create_or_update(request: web.Request, resource_group_name, hub_name, relationship_name, api_version, subscription_id, parameters) -> web.Response:
    """relationships_create_or_update

    Creates a relationship or updates an existing relationship within a hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param relationship_name: The name of the Relationship.
    :type relationship_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the CreateOrUpdate Relationship operation.
    :type parameters: dict | bytes

    """
    parameters = RelationshipResourceFormat.from_dict(parameters)
    return web.Response(status=200)


async def relationships_delete(request: web.Request, resource_group_name, hub_name, relationship_name, api_version, subscription_id) -> web.Response:
    """relationships_delete

    Deletes a relationship within a hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param relationship_name: The name of the relationship.
    :type relationship_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def relationships_get(request: web.Request, resource_group_name, hub_name, relationship_name, api_version, subscription_id) -> web.Response:
    """relationships_get

    Gets information about the specified relationship.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param relationship_name: The name of the relationship.
    :type relationship_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def relationships_list_by_hub(request: web.Request, resource_group_name, hub_name, api_version, subscription_id) -> web.Response:
    """relationships_list_by_hub

    Gets all relationships in the hub.

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
