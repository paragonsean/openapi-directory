from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.premium_messaging_regions_list_result import PremiumMessagingRegionsListResult
from openapi_server import util


async def regions_list_by_sku(request: web.Request, api_version, subscription_id, sku) -> web.Response:
    """regions_list_by_sku

    Gets the available Regions for a given sku

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param sku: The sku type.
    :type sku: str

    """
    return web.Response(status=200)
