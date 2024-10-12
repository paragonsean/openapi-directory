from typing import List, Dict
from aiohttp import web

from openapi_server.models.dedicated_host_list_result import DedicatedHostListResult
from openapi_server import util


async def dedicated_hosts_list_by_host_group(request: web.Request, resource_group_name, host_group_name, api_version, subscription_id) -> web.Response:
    """dedicated_hosts_list_by_host_group

    Lists all of the dedicated hosts in the specified dedicated host group. Use the nextLink property in the response to get the next page of dedicated hosts.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param host_group_name: The name of the dedicated host group.
    :type host_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
