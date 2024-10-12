from typing import List, Dict
from aiohttp import web

from openapi_server.models.sku_list_result import SkuListResult
from openapi_server import util


async def skus_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """skus_list

    Lists the available commitment plan SKUs.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: The version of the Microsoft.MachineLearning resource provider API to use.
    :type api_version: str

    """
    return web.Response(status=200)
