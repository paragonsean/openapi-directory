from typing import List, Dict
from aiohttp import web

from openapi_server.models.management_lock_list_result import ManagementLockListResult
from openapi_server.models.management_lock_object import ManagementLockObject
from openapi_server import util


async def management_locks_create_or_update_at_resource_group_level(request: web.Request, resource_group_name, lock_name, api_version, subscription_id, parameters) -> web.Response:
    """Creates or updates a management lock at the resource group level.

    When you apply a lock at a parent scope, all child resources inherit the same lock. To create management locks, you must have access to Microsoft.Authorization/* or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

    :param resource_group_name: The name of the resource group to lock.
    :type resource_group_name: str
    :param lock_name: The lock name. The lock name can be a maximum of 260 characters. It cannot contain &lt;, &gt; %, &amp;, :, \\, ?, /, or any control characters.
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
    """Creates or updates a management lock at the resource level or any level below the resource.

    When you apply a lock at a parent scope, all child resources inherit the same lock. To create management locks, you must have access to Microsoft.Authorization/* or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

    :param resource_group_name: The name of the resource group containing the resource to lock. 
    :type resource_group_name: str
    :param resource_provider_namespace: The resource provider namespace of the resource to lock.
    :type resource_provider_namespace: str
    :param parent_resource_path: The parent resource identity.
    :type parent_resource_path: str
    :param resource_type: The resource type of the resource to lock.
    :type resource_type: str
    :param resource_name: The name of the resource to lock.
    :type resource_name: str
    :param lock_name: The name of lock. The lock name can be a maximum of 260 characters. It cannot contain &lt;, &gt; %, &amp;, :, \\, ?, /, or any control characters.
    :type lock_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Parameters for creating or updating a  management lock.
    :type parameters: dict | bytes

    """
    parameters = ManagementLockObject.from_dict(parameters)
    return web.Response(status=200)


async def management_locks_create_or_update_at_subscription_level(request: web.Request, lock_name, api_version, subscription_id, parameters) -> web.Response:
    """Creates or updates a management lock at the subscription level.

    When you apply a lock at a parent scope, all child resources inherit the same lock. To create management locks, you must have access to Microsoft.Authorization/* or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

    :param lock_name: The name of lock. The lock name can be a maximum of 260 characters. It cannot contain &lt;, &gt; %, &amp;, :, \\, ?, /, or any control characters.
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


async def management_locks_create_or_update_by_scope(request: web.Request, scope, lock_name, api_version, parameters) -> web.Response:
    """management_locks_create_or_update_by_scope

    Create or update a management lock by scope.

    :param scope: The scope for the lock. When providing a scope for the assignment, use &#39;/subscriptions/{subscriptionId}&#39; for subscriptions, &#39;/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}&#39; for resource groups, and &#39;/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePathIfPresent}/{resourceType}/{resourceName}&#39; for resources.
    :type scope: str
    :param lock_name: The name of lock.
    :type lock_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param parameters: Create or update management lock parameters.
    :type parameters: dict | bytes

    """
    parameters = ManagementLockObject.from_dict(parameters)
    return web.Response(status=200)


async def management_locks_delete_at_resource_group_level(request: web.Request, resource_group_name, lock_name, api_version, subscription_id) -> web.Response:
    """Deletes a management lock at the resource group level.

    To delete management locks, you must have access to Microsoft.Authorization/* or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

    :param resource_group_name: The name of the resource group containing the lock.
    :type resource_group_name: str
    :param lock_name: The name of lock to delete.
    :type lock_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def management_locks_delete_at_resource_level(request: web.Request, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, lock_name, api_version, subscription_id) -> web.Response:
    """Deletes the management lock of a resource or any level below the resource.

    To delete management locks, you must have access to Microsoft.Authorization/* or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

    :param resource_group_name: The name of the resource group containing the resource with the lock to delete. 
    :type resource_group_name: str
    :param resource_provider_namespace: The resource provider namespace of the resource with the lock to delete.
    :type resource_provider_namespace: str
    :param parent_resource_path: The parent resource identity.
    :type parent_resource_path: str
    :param resource_type: The resource type of the resource with the lock to delete.
    :type resource_type: str
    :param resource_name: The name of the resource with the lock to delete.
    :type resource_name: str
    :param lock_name: The name of the lock to delete.
    :type lock_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def management_locks_delete_at_subscription_level(request: web.Request, lock_name, api_version, subscription_id) -> web.Response:
    """Deletes the management lock at the subscription level.

    To delete management locks, you must have access to Microsoft.Authorization/* or Microsoft.Authorization/locks/* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

    :param lock_name: The name of lock to delete.
    :type lock_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def management_locks_delete_by_scope(request: web.Request, scope, lock_name, api_version) -> web.Response:
    """management_locks_delete_by_scope

    Delete a management lock by scope.

    :param scope: The scope for the lock. 
    :type scope: str
    :param lock_name: The name of lock.
    :type lock_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def management_locks_get_at_resource_group_level(request: web.Request, resource_group_name, lock_name, api_version, subscription_id) -> web.Response:
    """management_locks_get_at_resource_group_level

    Gets a management lock at the resource group level.

    :param resource_group_name: The name of the locked resource group.
    :type resource_group_name: str
    :param lock_name: The name of the lock to get.
    :type lock_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def management_locks_get_at_resource_level(request: web.Request, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, lock_name, api_version, subscription_id) -> web.Response:
    """management_locks_get_at_resource_level

    Get the management lock of a resource or any level below resource.

    :param resource_group_name: The name of the resource group. 
    :type resource_group_name: str
    :param resource_provider_namespace: The namespace of the resource provider.
    :type resource_provider_namespace: str
    :param parent_resource_path: An extra path parameter needed in some services, like SQL Databases.
    :type parent_resource_path: str
    :param resource_type: The type of the resource.
    :type resource_type: str
    :param resource_name: The name of the resource.
    :type resource_name: str
    :param lock_name: The name of lock.
    :type lock_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def management_locks_get_at_subscription_level(request: web.Request, lock_name, api_version, subscription_id) -> web.Response:
    """management_locks_get_at_subscription_level

    Gets a management lock at the subscription level.

    :param lock_name: The name of the lock to get.
    :type lock_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def management_locks_get_by_scope(request: web.Request, scope, lock_name, api_version) -> web.Response:
    """management_locks_get_by_scope

    Get a management lock by scope.

    :param scope: The scope for the lock. 
    :type scope: str
    :param lock_name: The name of lock.
    :type lock_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def management_locks_list_at_resource_group_level(request: web.Request, resource_group_name, api_version, subscription_id, filter=None) -> web.Response:
    """management_locks_list_at_resource_group_level

    Gets all the management locks for a resource group.

    :param resource_group_name: The name of the resource group containing the locks to get.
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

    Gets all the management locks for a resource or any level below resource.

    :param resource_group_name: The name of the resource group containing the locked resource. The name is case insensitive.
    :type resource_group_name: str
    :param resource_provider_namespace: The namespace of the resource provider.
    :type resource_provider_namespace: str
    :param parent_resource_path: The parent resource identity.
    :type parent_resource_path: str
    :param resource_type: The resource type of the locked resource.
    :type resource_type: str
    :param resource_name: The name of the locked resource.
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

    Gets all the management locks for a subscription.

    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)


async def management_locks_list_by_scope(request: web.Request, scope, api_version, filter=None) -> web.Response:
    """management_locks_list_by_scope

    Gets all the management locks for a scope.

    :param scope: The scope for the lock. When providing a scope for the assignment, use &#39;/subscriptions/{subscriptionId}&#39; for subscriptions, &#39;/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}&#39; for resource groups, and &#39;/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePathIfPresent}/{resourceType}/{resourceName}&#39; for resources.
    :type scope: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)
