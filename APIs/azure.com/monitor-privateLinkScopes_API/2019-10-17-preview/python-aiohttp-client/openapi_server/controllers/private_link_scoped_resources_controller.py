from typing import List, Dict
from aiohttp import web

from openapi_server.models.scoped_resource import ScopedResource
from openapi_server.models.scoped_resource_list_result import ScopedResourceListResult
from openapi_server import util


async def private_link_scoped_resources_create_or_update(request: web.Request, subscription_id, resource_group_name, api_version, scope_name, name, parameters) -> web.Response:
    """private_link_scoped_resources_create_or_update

    Approve or reject a private endpoint connection with a given name.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param scope_name: Name of the Azure Monitor PrivateLinkScope that will contain the datasource
    :type scope_name: str
    :param name: The name of the scoped resource object.
    :type name: str
    :param parameters: 
    :type parameters: dict | bytes

    """
    parameters = ScopedResource.from_dict(parameters)
    return web.Response(status=200)


async def private_link_scoped_resources_delete(request: web.Request, subscription_id, resource_group_name, api_version, scope_name, name) -> web.Response:
    """private_link_scoped_resources_delete

    Deletes a private endpoint connection with a given name.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param scope_name: Name of the Azure Monitor PrivateLinkScope that will contain the datasource
    :type scope_name: str
    :param name: The name of the scoped resource object.
    :type name: str

    """
    return web.Response(status=200)


async def private_link_scoped_resources_get(request: web.Request, subscription_id, resource_group_name, api_version, scope_name, name) -> web.Response:
    """private_link_scoped_resources_get

    Gets a scoped resource in a private link scope.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param scope_name: Name of the Azure Monitor PrivateLinkScope that will contain the datasource
    :type scope_name: str
    :param name: The name of the scoped resource object.
    :type name: str

    """
    return web.Response(status=200)


async def private_link_scoped_resources_list_by_private_link_scope(request: web.Request, subscription_id, resource_group_name, api_version, scope_name) -> web.Response:
    """private_link_scoped_resources_list_by_private_link_scope

    Gets all private endpoint connections on a private link scope.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param scope_name: Name of the Azure Monitor PrivateLinkScope that will contain the datasource
    :type scope_name: str

    """
    return web.Response(status=200)
