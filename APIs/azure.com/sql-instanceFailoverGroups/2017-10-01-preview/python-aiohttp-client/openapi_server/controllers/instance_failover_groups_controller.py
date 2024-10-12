from typing import List, Dict
from aiohttp import web

from openapi_server.models.instance_failover_group import InstanceFailoverGroup
from openapi_server.models.instance_failover_group_list_result import InstanceFailoverGroupListResult
from openapi_server import util


async def instance_failover_groups_create_or_update(request: web.Request, resource_group_name, location_name, failover_group_name, subscription_id, api_version, parameters) -> web.Response:
    """instance_failover_groups_create_or_update

    Creates or updates a failover group.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param location_name: The name of the region where the resource is located.
    :type location_name: str
    :param failover_group_name: The name of the failover group.
    :type failover_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The failover group parameters.
    :type parameters: dict | bytes

    """
    parameters = InstanceFailoverGroup.from_dict(parameters)
    return web.Response(status=200)


async def instance_failover_groups_delete(request: web.Request, resource_group_name, location_name, failover_group_name, subscription_id, api_version) -> web.Response:
    """instance_failover_groups_delete

    Deletes a failover group.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param location_name: The name of the region where the resource is located.
    :type location_name: str
    :param failover_group_name: The name of the failover group.
    :type failover_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def instance_failover_groups_failover(request: web.Request, resource_group_name, location_name, failover_group_name, subscription_id, api_version) -> web.Response:
    """instance_failover_groups_failover

    Fails over from the current primary managed instance to this managed instance.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param location_name: The name of the region where the resource is located.
    :type location_name: str
    :param failover_group_name: The name of the failover group.
    :type failover_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def instance_failover_groups_force_failover_allow_data_loss(request: web.Request, resource_group_name, location_name, failover_group_name, subscription_id, api_version) -> web.Response:
    """instance_failover_groups_force_failover_allow_data_loss

    Fails over from the current primary managed instance to this managed instance. This operation might result in data loss.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param location_name: The name of the region where the resource is located.
    :type location_name: str
    :param failover_group_name: The name of the failover group.
    :type failover_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def instance_failover_groups_get(request: web.Request, resource_group_name, location_name, failover_group_name, subscription_id, api_version) -> web.Response:
    """instance_failover_groups_get

    Gets a failover group.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param location_name: The name of the region where the resource is located.
    :type location_name: str
    :param failover_group_name: The name of the failover group.
    :type failover_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def instance_failover_groups_list_by_location(request: web.Request, resource_group_name, location_name, subscription_id, api_version) -> web.Response:
    """instance_failover_groups_list_by_location

    Lists the failover groups in a location.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param location_name: The name of the region where the resource is located.
    :type location_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)
