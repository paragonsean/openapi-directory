from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def usage_get_usage(request: web.Request, resource_group_name, environment_name, last_id, batch_size, subscription_id, api_version) -> web.Response:
    """Returns usage records for specified subscription and resource groups

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param environment_name: Environment name
    :type environment_name: str
    :param last_id: Last marker that was returned from the batch
    :type last_id: str
    :param batch_size: size of the batch to be returned.
    :type batch_size: int
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)
