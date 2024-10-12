from typing import List, Dict
from aiohttp import web

from openapi_server.models.virtual_machine_size_list_result import VirtualMachineSizeListResult
from openapi_server import util


async def virtual_machine_sizes_list(request: web.Request, location, api_version, subscription_id) -> web.Response:
    """virtual_machine_sizes_list

    This API is deprecated. Use [Resources Skus](https://docs.microsoft.com/en-us/rest/api/compute/resourceskus/list)

    :param location: The location upon which virtual-machine-sizes is queried.
    :type location: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
