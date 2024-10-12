from typing import List, Dict
from aiohttp import web

from openapi_server.models.managed_instance import ManagedInstance
from openapi_server.models.managed_instance_list_result import ManagedInstanceListResult
from openapi_server.models.managed_instance_update import ManagedInstanceUpdate
from openapi_server import util


async def managed_instances_create_or_update(request: web.Request, resource_group_name, managed_instance_name, subscription_id, api_version, parameters) -> web.Response:
    """managed_instances_create_or_update

    Creates or updates a managed instance.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param managed_instance_name: The name of the managed instance.
    :type managed_instance_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested managed instance resource state.
    :type parameters: dict | bytes

    """
    parameters = ManagedInstance.from_dict(parameters)
    return web.Response(status=200)


async def managed_instances_delete(request: web.Request, resource_group_name, managed_instance_name, subscription_id, api_version) -> web.Response:
    """managed_instances_delete

    Deletes a managed instance.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param managed_instance_name: The name of the managed instance.
    :type managed_instance_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def managed_instances_get(request: web.Request, resource_group_name, managed_instance_name, subscription_id, api_version) -> web.Response:
    """managed_instances_get

    Gets a managed instance.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param managed_instance_name: The name of the managed instance.
    :type managed_instance_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def managed_instances_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """managed_instances_list

    Gets a list of all managed instances in the subscription.

    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def managed_instances_list_by_resource_group(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """managed_instances_list_by_resource_group

    Gets a list of managed instances in a resource group.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def managed_instances_update(request: web.Request, resource_group_name, managed_instance_name, subscription_id, api_version, parameters) -> web.Response:
    """managed_instances_update

    Updates a managed instance.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param managed_instance_name: The name of the managed instance.
    :type managed_instance_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested managed instance resource state.
    :type parameters: dict | bytes

    """
    parameters = ManagedInstanceUpdate.from_dict(parameters)
    return web.Response(status=200)
