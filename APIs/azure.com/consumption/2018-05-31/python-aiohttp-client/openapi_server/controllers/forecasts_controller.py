from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.forecasts_list_result import ForecastsListResult
from openapi_server import util


async def forecasts_list(request: web.Request, api_version, subscription_id, filter=None) -> web.Response:
    """forecasts_list

    Lists the forecast charges by subscriptionId.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-05-31.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param filter: May be used to filter forecasts by properties/usageDate (Utc time), properties/chargeType or properties/grain. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;.
    :type filter: str

    """
    return web.Response(status=200)
