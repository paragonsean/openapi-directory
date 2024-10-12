from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def policies_delete(request: web.Request, resource_group_name, policy_name, subscription_id, api_version) -> web.Response:
    """policies_delete

    Deletes Policy

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param policy_name: The name of the resource group.
    :type policy_name: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)
