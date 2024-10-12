from typing import List, Dict
from aiohttp import web

from openapi_server.models.resource_type_sku_collection import ResourceTypeSkuCollection
from openapi_server import util


async def skus_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """skus_list

    Lists the Skus of the resource type.

    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
