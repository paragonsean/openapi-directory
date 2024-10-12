from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.usage_details_list_result import UsageDetailsListResult
from openapi_server import util


async def usage_details_list(request: web.Request, scope, api_version, expand=None, filter=None, skiptoken=None, top=None) -> web.Response:
    """usage_details_list

    Lists the usage details for a scope in reverse chronological order by billing period. Usage details are available via this API only for January 1, 2017 or later.

    :param scope: The scope of the usage details. The scope can be &#39;/subscriptions/{subscriptionId}&#39; for a subscription, or &#39;/subscriptions/{subscriptionId}/providers/Microsoft.Billing/invoices/{invoiceName}&#39; for an invoice or &#39;/subscriptions/{subscriptionId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}&#39; for a billing period.
    :type scope: str
    :param api_version: Version of the API to be used with the client request. The current version is 2017-02-27-preview.
    :type api_version: str
    :param expand: May be used to expand the additionalProperties or meterDetails property within a list of usage details. By default, these fields are not included when listing usage details.
    :type expand: str
    :param filter: May be used to filter usageDetails by usageEnd (Utc time). The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;.
    :type filter: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N usageDetails.
    :type top: int

    """
    return web.Response(status=200)
