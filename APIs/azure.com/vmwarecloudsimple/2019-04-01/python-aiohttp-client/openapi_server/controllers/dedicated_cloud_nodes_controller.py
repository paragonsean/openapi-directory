from typing import List, Dict
from aiohttp import web

from openapi_server.models.csrp_error import CSRPError
from openapi_server.models.dedicated_cloud_node import DedicatedCloudNode
from openapi_server.models.dedicated_cloud_node_list_response import DedicatedCloudNodeListResponse
from openapi_server.models.patch_payload import PatchPayload
from openapi_server import util


async def dedicated_cloud_nodes_create_or_update(request: web.Request, subscription_id, resource_group_name, referer, dedicated_cloud_node_name, api_version, dedicated_cloud_node_request) -> web.Response:
    """Implements dedicated cloud node PUT method

    Returns dedicated cloud node by its name

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group
    :type resource_group_name: str
    :param referer: referer url
    :type referer: str
    :param dedicated_cloud_node_name: dedicated cloud node name
    :type dedicated_cloud_node_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param dedicated_cloud_node_request: Create Dedicated Cloud Node request
    :type dedicated_cloud_node_request: dict | bytes

    """
    dedicated_cloud_node_request = DedicatedCloudNode.from_dict(dedicated_cloud_node_request)
    return web.Response(status=200)


async def dedicated_cloud_nodes_delete(request: web.Request, subscription_id, resource_group_name, dedicated_cloud_node_name, api_version) -> web.Response:
    """Implements dedicated cloud node DELETE method

    Delete dedicated cloud node

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group
    :type resource_group_name: str
    :param dedicated_cloud_node_name: dedicated cloud node name
    :type dedicated_cloud_node_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def dedicated_cloud_nodes_get(request: web.Request, subscription_id, resource_group_name, dedicated_cloud_node_name, api_version) -> web.Response:
    """Implements dedicated cloud node GET method

    Returns dedicated cloud node

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group
    :type resource_group_name: str
    :param dedicated_cloud_node_name: dedicated cloud node name
    :type dedicated_cloud_node_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def dedicated_cloud_nodes_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version, filter=None, top=None, skip_token=None) -> web.Response:
    """Implements list of dedicated cloud nodes within RG method

    Returns list of dedicate cloud nodes within resource group

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param filter: The filter to apply on the list operation
    :type filter: str
    :param top: The maximum number of record sets to return
    :type top: int
    :param skip_token: to be used by nextLink implementation
    :type skip_token: str

    """
    return web.Response(status=200)


async def dedicated_cloud_nodes_list_by_subscription(request: web.Request, subscription_id, api_version, filter=None, top=None, skip_token=None) -> web.Response:
    """Implements list of dedicated cloud nodes within subscription method

    Returns list of dedicate cloud nodes within subscription

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param filter: The filter to apply on the list operation
    :type filter: str
    :param top: The maximum number of record sets to return
    :type top: int
    :param skip_token: to be used by nextLink implementation
    :type skip_token: str

    """
    return web.Response(status=200)


async def dedicated_cloud_nodes_update(request: web.Request, subscription_id, resource_group_name, dedicated_cloud_node_name, api_version, dedicated_cloud_node_request) -> web.Response:
    """Implements dedicated cloud node PATCH method

    Patches dedicated node properties

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group
    :type resource_group_name: str
    :param dedicated_cloud_node_name: dedicated cloud node name
    :type dedicated_cloud_node_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param dedicated_cloud_node_request: Patch Dedicated Cloud Node request
    :type dedicated_cloud_node_request: dict | bytes

    """
    dedicated_cloud_node_request = PatchPayload.from_dict(dedicated_cloud_node_request)
    return web.Response(status=200)
