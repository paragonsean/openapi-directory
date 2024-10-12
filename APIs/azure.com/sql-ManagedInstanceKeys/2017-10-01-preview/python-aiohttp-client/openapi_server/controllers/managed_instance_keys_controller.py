from typing import List, Dict
from aiohttp import web

from openapi_server.models.managed_instance_key import ManagedInstanceKey
from openapi_server.models.managed_instance_key_list_result import ManagedInstanceKeyListResult
from openapi_server import util


async def managed_instance_keys_create_or_update(request: web.Request, resource_group_name, managed_instance_name, key_name, subscription_id, api_version, parameters) -> web.Response:
    """managed_instance_keys_create_or_update

    Creates or updates a managed instance key.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param managed_instance_name: The name of the managed instance.
    :type managed_instance_name: str
    :param key_name: The name of the managed instance key to be operated on (updated or created).
    :type key_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested managed instance key resource state.
    :type parameters: dict | bytes

    """
    parameters = ManagedInstanceKey.from_dict(parameters)
    return web.Response(status=200)


async def managed_instance_keys_delete(request: web.Request, resource_group_name, managed_instance_name, key_name, subscription_id, api_version) -> web.Response:
    """managed_instance_keys_delete

    Deletes the managed instance key with the given name.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param managed_instance_name: The name of the managed instance.
    :type managed_instance_name: str
    :param key_name: The name of the managed instance key to be deleted.
    :type key_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def managed_instance_keys_get(request: web.Request, resource_group_name, managed_instance_name, key_name, subscription_id, api_version) -> web.Response:
    """managed_instance_keys_get

    Gets a managed instance key.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param managed_instance_name: The name of the managed instance.
    :type managed_instance_name: str
    :param key_name: The name of the managed instance key to be retrieved.
    :type key_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def managed_instance_keys_list_by_instance(request: web.Request, resource_group_name, managed_instance_name, subscription_id, api_version, filter=None) -> web.Response:
    """managed_instance_keys_list_by_instance

    Gets a list of managed instance keys.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param managed_instance_name: The name of the managed instance.
    :type managed_instance_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param filter: An OData filter expression that filters elements in the collection.
    :type filter: str

    """
    return web.Response(status=200)
