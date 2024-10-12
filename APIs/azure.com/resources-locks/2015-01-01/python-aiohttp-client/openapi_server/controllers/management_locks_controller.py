from typing import List, Dict
from aiohttp import web

from openapi_server.models.management_lock_list_result import ManagementLockListResult
from openapi_server.models.management_lock_object import ManagementLockObject
from openapi_server import util


async def management_locks_create_or_update_at_resource_group_level(request: web.Request, resource_group_name, lock_name, api_version, subscription_id, parameters) -> web.Response:
    """management_locks_create_or_update_at_resource_group_level

    Create or update a management lock at the resource group level.

    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param lock_name: The lock name.
    :type lock_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: The management lock parameters.
    :type parameters: dict | bytes

    """
    parameters = ManagementLockObject.from_dict(parameters)
    return web.Response(status=200)


async def management_locks_create_or_update_at_resource_level(request: web.Request, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, lock_name, api_version, subscription_id, parameters) -> web.Response:
    """management_locks_create_or_update_at_resource_level

    Create or update a management lock at the resource level or any level below resource.

    :param resource_group_name: The name of the resource group. 
    :type resource_group_name: str
    :param resource_provider_namespace: Resource identity.
    :type resource_provider_namespace: str
    :param parent_resource_path: Resource identity.
    :type parent_resource_path: str
    :param resource_type: Resource identity.
    :type resource_type: str
    :param resource_name: Resource identity.
    :type resource_name: str
    :param lock_name: The name of lock.
    :type lock_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Create or update management lock parameters.
    :type parameters: dict | bytes

    """
    parameters = ManagementLockObject.from_dict(parameters)
    return web.Response(status=200)


async def management_locks_create_or_update_at_subscription_level(request: web.Request, lock_name, api_version, subscription_id, parameters) -> web.Response:
    """management_locks_create_or_update_at_subscription_level

    Create or update a management lock at the subscription level.

    :param lock_name: The name of lock.
    :type lock_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: The management lock parameters.
    :type parameters: dict | bytes

    """
    parameters = ManagementLockObject.from_dict(parameters)
    return web.Response(status=200)


async def management_locks_delete_at_resource_group_level(request: web.Request, resource_group_name, lock_name, api_version, subscription_id) -> web.Response:
    """management_locks_delete_at_resource_group_level

    Deletes the management lock of a resource group.

    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param lock_name: The name of lock.
    :type lock_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def management_locks_delete_at_resource_level(request: web.Request, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, lock_name, api_version, subscription_id) -> web.Response:
    """management_locks_delete_at_resource_level

    Deletes the management lock of a resource or any level below resource.

    :param resource_group_name: The name of the resource group. 
    :type resource_group_name: str
    :param resource_provider_namespace: Resource identity.
    :type resource_provider_namespace: str
    :param parent_resource_path: Resource identity.
    :type parent_resource_path: str
    :param resource_type: Resource identity.
    :type resource_type: str
    :param resource_name: Resource identity.
    :type resource_name: str
    :param lock_name: The name of lock.
    :type lock_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def management_locks_delete_at_subscription_level(request: web.Request, lock_name, api_version, subscription_id) -> web.Response:
    """management_locks_delete_at_subscription_level

    Deletes the management lock of a subscription.

    :param lock_name: The name of lock.
    :type lock_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def management_locks_get(request: web.Request, lock_name, api_version, subscription_id) -> web.Response:
    """management_locks_get

    Gets the management lock of a scope.

    :param lock_name: Name of the management lock.
    :type lock_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def management_locks_get_at_resource_group_level(request: web.Request, resource_group_name, lock_name, api_version, subscription_id) -> web.Response:
    """management_locks_get_at_resource_group_level

    Gets a management lock at the resource group level.

    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param lock_name: The lock name.
    :type lock_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def management_locks_list_at_resource_group_level(request: web.Request, resource_group_name, api_version, subscription_id, filter=None) -> web.Response:
    """management_locks_list_at_resource_group_level

    Gets all the management locks of a resource group.

    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)


async def management_locks_list_at_resource_level(request: web.Request, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, subscription_id, filter=None) -> web.Response:
    """management_locks_list_at_resource_level

    Gets all the management locks of a resource or any level below resource.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param resource_provider_namespace: Resource identity.
    :type resource_provider_namespace: str
    :param parent_resource_path: Resource identity.
    :type parent_resource_path: str
    :param resource_type: Resource identity.
    :type resource_type: str
    :param resource_name: Resource identity.
    :type resource_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)


async def management_locks_list_at_subscription_level(request: web.Request, api_version, subscription_id, filter=None) -> web.Response:
    """management_locks_list_at_subscription_level

    Gets all the management locks of a subscription.

    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)
