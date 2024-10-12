from typing import List, Dict
from aiohttp import web

from openapi_server.models.billing_period import BillingPeriod
from openapi_server.models.billing_periods_list_result import BillingPeriodsListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def billing_periods_get(request: web.Request, subscription_id, api_version, billing_period_name) -> web.Response:
    """billing_periods_get

    Gets a named billing period.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2017-04-24-preview.
    :type api_version: str
    :param billing_period_name: The name of a BillingPeriod resource.
    :type billing_period_name: str

    """
    return web.Response(status=200)


async def billing_periods_list(request: web.Request, subscription_id, api_version, filter=None, skiptoken=None, top=None) -> web.Response:
    """billing_periods_list

    Lists the available billing periods for a subscription in reverse chronological order.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2017-04-24-preview.
    :type api_version: str
    :param filter: May be used to filter billing periods by billingPeriodEndDate. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;.
    :type filter: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N billing periods.
    :type top: int

    """
    return web.Response(status=200)
