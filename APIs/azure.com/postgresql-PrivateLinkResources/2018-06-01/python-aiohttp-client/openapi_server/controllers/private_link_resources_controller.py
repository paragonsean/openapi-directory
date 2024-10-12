from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.private_link_resource import PrivateLinkResource
from openapi_server.models.private_link_resource_list_result import PrivateLinkResourceListResult
from openapi_server import util


async def private_link_resources_get(request: web.Request, resource_group_name, server_name, group_name, subscription_id, api_version) -> web.Response:
    """private_link_resources_get

    Gets a private link resource for PostgreSQL server.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param group_name: The name of the private link resource.
    :type group_name: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def private_link_resources_list_by_server(request: web.Request, resource_group_name, server_name, subscription_id, api_version) -> web.Response:
    """private_link_resources_list_by_server

    Gets the private link resources for PostgreSQL server.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)
