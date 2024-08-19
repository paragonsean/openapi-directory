from typing import List, Dict
from aiohttp import web

from openapi_server.models.private_link_resource import PrivateLinkResource
from openapi_server.models.private_link_resource_list_result import PrivateLinkResourceListResult
from openapi_server import util


async def private_link_resources_get(request: web.Request, subscription_id, resource_group_name, api_version, scope_name, group_name) -> web.Response:
    """private_link_resources_get

    Gets the private link resources that need to be created for a Azure Monitor PrivateLinkScope.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param scope_name: Name of the Azure Monitor PrivateLinkScope that will contain the datasource
    :type scope_name: str
    :param group_name: The name of the private link resource.
    :type group_name: str

    """
    return web.Response(status=200)


async def private_link_resources_list_by_private_link_scope(request: web.Request, subscription_id, resource_group_name, api_version, scope_name) -> web.Response:
    """private_link_resources_list_by_private_link_scope

    Gets the private link resources that need to be created for a Azure Monitor PrivateLinkScope.

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
