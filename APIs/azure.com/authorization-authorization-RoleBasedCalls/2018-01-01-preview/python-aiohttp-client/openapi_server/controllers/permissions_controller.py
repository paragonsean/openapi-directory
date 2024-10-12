from typing import List, Dict
from aiohttp import web

from openapi_server.models.permission_get_result import PermissionGetResult
from openapi_server import util


async def permissions_list_for_resource(request: web.Request, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, subscription_id) -> web.Response:
    """permissions_list_for_resource

    Gets all permissions the caller has for a resource.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_provider_namespace: The namespace of the resource provider.
    :type resource_provider_namespace: str
    :param parent_resource_path: The parent resource identity.
    :type parent_resource_path: str
    :param resource_type: The resource type of the resource.
    :type resource_type: str
    :param resource_name: The name of the resource to get the permissions for.
    :type resource_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def permissions_list_for_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """permissions_list_for_resource_group

    Gets all permissions the caller has for a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)
