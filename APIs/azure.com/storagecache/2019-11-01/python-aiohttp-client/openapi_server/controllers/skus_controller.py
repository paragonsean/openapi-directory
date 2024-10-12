from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.resource_skus_result import ResourceSkusResult
from openapi_server import util


async def skus_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """skus_list

    Get the list of StorageCache.Cache SKUs available to this subscription.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
