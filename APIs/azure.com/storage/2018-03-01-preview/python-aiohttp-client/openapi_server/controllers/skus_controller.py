from typing import List, Dict
from aiohttp import web

from openapi_server.models.storage_sku_list_result import StorageSkuListResult
from openapi_server import util


async def skus_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """skus_list

    Lists the available SKUs supported by Microsoft.Storage for given subscription.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)
