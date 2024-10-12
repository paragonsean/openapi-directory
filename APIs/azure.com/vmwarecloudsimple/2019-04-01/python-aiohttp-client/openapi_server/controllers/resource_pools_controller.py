from typing import List, Dict
from aiohttp import web

from openapi_server.models.csrp_error import CSRPError
from openapi_server.models.resource_pool import ResourcePool
from openapi_server.models.resource_pools_list_response import ResourcePoolsListResponse
from openapi_server import util


async def resource_pools_get(request: web.Request, subscription_id, api_version, region_id, pc_name, resource_pool_name) -> web.Response:
    """Implements get of resource pool

    Returns resource pool templates by its name

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param region_id: The region Id (westus, eastus)
    :type region_id: str
    :param pc_name: The private cloud name
    :type pc_name: str
    :param resource_pool_name: resource pool id (vsphereId)
    :type resource_pool_name: str

    """
    return web.Response(status=200)


async def resource_pools_list(request: web.Request, subscription_id, region_id, pc_name, api_version) -> web.Response:
    """Implements get of resource pools list

    Returns list of resource pools in region for private cloud

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param region_id: The region Id (westus, eastus)
    :type region_id: str
    :param pc_name: The private cloud name
    :type pc_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)
