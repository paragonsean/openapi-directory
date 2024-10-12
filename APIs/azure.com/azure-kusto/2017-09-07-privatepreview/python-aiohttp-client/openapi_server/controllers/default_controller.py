from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.list_skus_result import ListSkusResult
from openapi_server import util


async def clusters_list_skus(request: web.Request, api_version, subscription_id) -> web.Response:
    """clusters_list_skus

    Lists eligible SKUs for Kusto resource provider.

    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
