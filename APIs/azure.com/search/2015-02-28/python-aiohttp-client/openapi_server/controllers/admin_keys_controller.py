from typing import List, Dict
from aiohttp import web

from openapi_server.models.admin_key_result import AdminKeyResult
from openapi_server import util


async def admin_keys_list(request: web.Request, resource_group_name, service_name, api_version, subscription_id) -> web.Response:
    """admin_keys_list

    Returns the primary and secondary API keys for the given Azure Search service.

    :param resource_group_name: The name of the resource group within the current subscription.
    :type resource_group_name: str
    :param service_name: The name of the Search service for which to list admin keys.
    :type service_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
