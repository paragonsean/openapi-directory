from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.premium_messaging_regions_list_result import PremiumMessagingRegionsListResult
from openapi_server import util


async def premium_messaging_regions_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """premium_messaging_regions_list

    Gets the available premium messaging regions for servicebus 

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
