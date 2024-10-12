from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.sku_description_list import SkuDescriptionList
from openapi_server import util


async def s_kus_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """List available SKUs of EngagementFabric resource

    

    :param subscription_id: Subscription ID
    :type subscription_id: str
    :param api_version: API version
    :type api_version: str

    """
    return web.Response(status=200)
