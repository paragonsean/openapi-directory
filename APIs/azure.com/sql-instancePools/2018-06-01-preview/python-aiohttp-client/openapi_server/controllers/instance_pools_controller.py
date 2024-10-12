from typing import List, Dict
from aiohttp import web

from openapi_server.models.instance_pool import InstancePool
from openapi_server.models.instance_pool_list_result import InstancePoolListResult
from openapi_server.models.instance_pool_update import InstancePoolUpdate
from openapi_server import util


async def instance_pools_create_or_update(request: web.Request, resource_group_name, instance_pool_name, subscription_id, api_version, parameters) -> web.Response:
    """instance_pools_create_or_update

    Creates or updates an instance pool.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param instance_pool_name: The name of the instance pool to be created or updated.
    :type instance_pool_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested instance pool resource state.
    :type parameters: dict | bytes

    """
    parameters = InstancePool.from_dict(parameters)
    return web.Response(status=200)


async def instance_pools_delete(request: web.Request, resource_group_name, instance_pool_name, subscription_id, api_version) -> web.Response:
    """instance_pools_delete

    Deletes an instance pool

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param instance_pool_name: The name of the instance pool to be deleted
    :type instance_pool_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def instance_pools_get(request: web.Request, resource_group_name, instance_pool_name, subscription_id, api_version) -> web.Response:
    """instance_pools_get

    Gets an instance pool.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param instance_pool_name: The name of the instance pool to be retrieved.
    :type instance_pool_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def instance_pools_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """instance_pools_list

    Gets a list of all instance pools in the subscription.

    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def instance_pools_list_by_resource_group(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """instance_pools_list_by_resource_group

    Gets a list of instance pools in the resource group

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def instance_pools_update(request: web.Request, resource_group_name, instance_pool_name, subscription_id, api_version, parameters) -> web.Response:
    """instance_pools_update

    Updates an instance pool.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param instance_pool_name: The name of the instance pool to be updated.
    :type instance_pool_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested instance pool resource state.
    :type parameters: dict | bytes

    """
    parameters = InstancePoolUpdate.from_dict(parameters)
    return web.Response(status=200)
