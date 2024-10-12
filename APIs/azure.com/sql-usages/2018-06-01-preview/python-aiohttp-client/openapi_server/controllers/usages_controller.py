from typing import List, Dict
from aiohttp import web

from openapi_server.models.usage_list_result import UsageListResult
from openapi_server import util


async def usages_list_by_instance_pool(request: web.Request, resource_group_name, instance_pool_name, subscription_id, api_version, expand_children=None) -> web.Response:
    """usages_list_by_instance_pool

    Gets all instance pool usage metrics

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param instance_pool_name: The name of the instance pool to be retrieved.
    :type instance_pool_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param expand_children: Optional request parameter to include managed instance usages within the instance pool.
    :type expand_children: bool

    """
    return web.Response(status=200)
