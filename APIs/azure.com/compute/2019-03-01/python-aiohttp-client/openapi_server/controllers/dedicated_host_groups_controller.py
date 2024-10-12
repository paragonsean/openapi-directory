from typing import List, Dict
from aiohttp import web

from openapi_server.models.dedicated_host_group import DedicatedHostGroup
from openapi_server.models.dedicated_host_group_list_result import DedicatedHostGroupListResult
from openapi_server.models.dedicated_host_group_update import DedicatedHostGroupUpdate
from openapi_server import util


async def dedicated_host_groups_create_or_update(request: web.Request, resource_group_name, host_group_name, api_version, subscription_id, parameters) -> web.Response:
    """dedicated_host_groups_create_or_update

    Create or update a dedicated host group. For details of Dedicated Host and Dedicated Host Groups please see [Dedicated Host Documentation] (https://go.microsoft.com/fwlink/?linkid&#x3D;2082596)

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param host_group_name: The name of the dedicated host group.
    :type host_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Create Dedicated Host Group.
    :type parameters: dict | bytes

    """
    parameters = DedicatedHostGroup.from_dict(parameters)
    return web.Response(status=200)


async def dedicated_host_groups_delete(request: web.Request, resource_group_name, host_group_name, api_version, subscription_id) -> web.Response:
    """dedicated_host_groups_delete

    Delete a dedicated host group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param host_group_name: The name of the dedicated host group.
    :type host_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def dedicated_host_groups_get(request: web.Request, resource_group_name, host_group_name, api_version, subscription_id) -> web.Response:
    """dedicated_host_groups_get

    Retrieves information about a dedicated host group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param host_group_name: The name of the dedicated host group.
    :type host_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def dedicated_host_groups_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """dedicated_host_groups_list_by_resource_group

    Lists all of the dedicated host groups in the specified resource group. Use the nextLink property in the response to get the next page of dedicated host groups.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def dedicated_host_groups_list_by_subscription(request: web.Request, api_version, subscription_id) -> web.Response:
    """dedicated_host_groups_list_by_subscription

    Lists all of the dedicated host groups in the subscription. Use the nextLink property in the response to get the next page of dedicated host groups.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def dedicated_host_groups_update(request: web.Request, resource_group_name, host_group_name, api_version, subscription_id, parameters) -> web.Response:
    """dedicated_host_groups_update

    Update an dedicated host group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param host_group_name: The name of the dedicated host group.
    :type host_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Update Dedicated Host Group operation.
    :type parameters: dict | bytes

    """
    parameters = DedicatedHostGroupUpdate.from_dict(parameters)
    return web.Response(status=200)
