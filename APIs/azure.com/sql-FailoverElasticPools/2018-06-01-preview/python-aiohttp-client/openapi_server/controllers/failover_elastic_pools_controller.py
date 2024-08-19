from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def elastic_pools_failover(request: web.Request, resource_group_name, server_name, elastic_pool_name, subscription_id, api_version) -> web.Response:
    """elastic_pools_failover

    Failovers an elastic pool.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param elastic_pool_name: The name of the elastic pool to failover.
    :type elastic_pool_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)
