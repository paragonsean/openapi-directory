from typing import List, Dict
from aiohttp import web

from openapi_server.models.sku_enumeration_for_new_resource_result import SkuEnumerationForNewResourceResult
from openapi_server import util


async def capacities_list_skus(request: web.Request, api_version, subscription_id) -> web.Response:
    """capacities_list_skus

    Lists eligible SKUs for PowerBI Dedicated resource provider.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
