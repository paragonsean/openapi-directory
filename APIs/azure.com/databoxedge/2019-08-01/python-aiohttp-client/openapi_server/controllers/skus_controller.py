from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.sku_information_list import SkuInformationList
from openapi_server import util


async def skus_list(request: web.Request, subscription_id, api_version, filter=None) -> web.Response:
    """List all the available Skus in the region and information related to them

    

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param api_version: The API version.
    :type api_version: str
    :param filter: Specify $filter&#x3D;&#39;location eq &lt;location&gt;&#39; to filter on location.
    :type filter: str

    """
    return web.Response(status=200)
