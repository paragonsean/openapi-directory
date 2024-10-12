from typing import List, Dict
from aiohttp import web

from openapi_server.models.sku_enumeration_for_new_resource_result import SkuEnumerationForNewResourceResult
from openapi_server import util


async def servers_list_skus_for_new(request: web.Request, api_version, subscription_id) -> web.Response:
    """servers_list_skus_for_new

    Lists eligible SKUs for Analysis Services resource provider.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
