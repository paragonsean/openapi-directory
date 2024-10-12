from typing import List, Dict
from aiohttp import web

from openapi_server.models.ip_group import IpGroup
from openapi_server.models.ip_group_list_result import IpGroupListResult
from openapi_server.models.ip_groups_list_default_response import IpGroupsListDefaultResponse
from openapi_server.models.ip_groups_update_groups_request import IpGroupsUpdateGroupsRequest
from openapi_server import util


async def ip_groups_create_or_update(request: web.Request, resource_group_name, ip_groups_name, api_version, subscription_id, parameters) -> web.Response:
    """ip_groups_create_or_update

    Creates or updates an ipGroups in a specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param ip_groups_name: The name of the ipGroups.
    :type ip_groups_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update IpGroups operation.
    :type parameters: dict | bytes

    """
    parameters = IpGroup.from_dict(parameters)
    return web.Response(status=200)


async def ip_groups_delete(request: web.Request, resource_group_name, ip_groups_name, api_version, subscription_id) -> web.Response:
    """ip_groups_delete

    Deletes the specified ipGroups.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param ip_groups_name: The name of the ipGroups.
    :type ip_groups_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def ip_groups_get(request: web.Request, resource_group_name, ip_groups_name, api_version, subscription_id, expand=None) -> web.Response:
    """ip_groups_get

    Gets the specified ipGroups.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param ip_groups_name: The name of the ipGroups.
    :type ip_groups_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: Expands resourceIds (of Firewalls/Network Security Groups etc.) back referenced by the IpGroups resource.
    :type expand: str

    """
    return web.Response(status=200)


async def ip_groups_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """ip_groups_list

    Gets all IpGroups in a subscription.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def ip_groups_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """ip_groups_list_by_resource_group

    Gets all IpGroups in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def ip_groups_update_groups(request: web.Request, resource_group_name, ip_groups_name, api_version, subscription_id, parameters) -> web.Response:
    """ip_groups_update_groups

    Updates tags of an IpGroups resource.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param ip_groups_name: The name of the ipGroups.
    :type ip_groups_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the update ipGroups operation.
    :type parameters: dict | bytes

    """
    parameters = IpGroupsUpdateGroupsRequest.from_dict(parameters)
    return web.Response(status=200)
