from typing import List, Dict
from aiohttp import web

from openapi_server.models.azure_monitor_private_link_scope import AzureMonitorPrivateLinkScope
from openapi_server.models.azure_monitor_private_link_scope_list_result import AzureMonitorPrivateLinkScopeListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tags_resource import TagsResource
from openapi_server import util


async def private_link_scopes_create_or_update(request: web.Request, resource_group_name, api_version, subscription_id, scope_name, azure_monitor_private_link_scope_payload) -> web.Response:
    """private_link_scopes_create_or_update

    Creates (or updates) a Azure Monitor PrivateLinkScope. Note: You cannot specify a different value for InstrumentationKey nor AppId in the Put operation.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param scope_name: The name of the Azure Monitor PrivateLinkScope resource.
    :type scope_name: str
    :param azure_monitor_private_link_scope_payload: Properties that need to be specified to create or update a Azure Monitor PrivateLinkScope.
    :type azure_monitor_private_link_scope_payload: dict | bytes

    """
    azure_monitor_private_link_scope_payload = AzureMonitorPrivateLinkScope.from_dict(azure_monitor_private_link_scope_payload)
    return web.Response(status=200)


async def private_link_scopes_delete(request: web.Request, resource_group_name, api_version, subscription_id, scope_name) -> web.Response:
    """private_link_scopes_delete

    Deletes a Azure Monitor PrivateLinkScope.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param scope_name: The name of the Azure Monitor PrivateLinkScope resource.
    :type scope_name: str

    """
    return web.Response(status=200)


async def private_link_scopes_get(request: web.Request, resource_group_name, api_version, subscription_id, scope_name) -> web.Response:
    """private_link_scopes_get

    Returns a Azure Monitor PrivateLinkScope.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param scope_name: The name of the Azure Monitor PrivateLinkScope resource.
    :type scope_name: str

    """
    return web.Response(status=200)


async def private_link_scopes_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """private_link_scopes_list

    Gets a list of all Azure Monitor PrivateLinkScopes within a subscription.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def private_link_scopes_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """private_link_scopes_list_by_resource_group

    Gets a list of Azure Monitor PrivateLinkScopes within a resource group.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def private_link_scopes_update_tags(request: web.Request, resource_group_name, api_version, subscription_id, scope_name, private_link_scope_tags) -> web.Response:
    """private_link_scopes_update_tags

    Updates an existing PrivateLinkScope&#39;s tags. To update other fields use the CreateOrUpdate method.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param scope_name: The name of the Azure Monitor PrivateLinkScope resource.
    :type scope_name: str
    :param private_link_scope_tags: Updated tag information to set into the PrivateLinkScope instance.
    :type private_link_scope_tags: dict | bytes

    """
    private_link_scope_tags = TagsResource.from_dict(private_link_scope_tags)
    return web.Response(status=200)
