from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.cost import Cost
from openapi_server.models.response_with_continuation_cost import ResponseWithContinuationCost
from openapi_server import util


async def cost_get_resource(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """cost_get_resource

    Get cost.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the cost.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def cost_list(request: web.Request, subscription_id, resource_group_name, lab_name, api_version, filter=None, top=None, order_by=None) -> web.Response:
    """cost_list

    List costs.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: 
    :type top: int
    :param order_by: 
    :type order_by: str

    """
    return web.Response(status=200)


async def cost_refresh_data(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """cost_refresh_data

    Refresh Lab&#39;s Cost Data. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the cost.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)
