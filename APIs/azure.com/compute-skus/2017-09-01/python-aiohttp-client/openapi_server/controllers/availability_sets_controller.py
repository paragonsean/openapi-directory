from typing import List, Dict
from aiohttp import web

from openapi_server.models.resource_skus_result import ResourceSkusResult
from openapi_server import util


async def resource_skus_list_0(request: web.Request, api_version, subscription_id) -> web.Response:
    """resource_skus_list_0

    Gets the list of Microsoft.Compute SKUs available for your Subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
