from typing import List, Dict
from aiohttp import web

from openapi_server.models.charge_summary import ChargeSummary
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def charges_list_by_scope(request: web.Request, scope, api_version, filter=None) -> web.Response:
    """charges_list_by_scope

    Lists the charges based for the defined scope.

    :param scope: The scope associated with usage details operations. This includes &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope and &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope. For department and enrollment accounts, you can also add billing period to the scope using &#39;/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}&#39;. For e.g. to specify billing period at department scope use &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}&#39;
    :type scope: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-01-01.
    :type api_version: str
    :param filter: May be used to filter charges by properties/usageEnd (Utc time), properties/usageStart (Utc time). The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str

    """
    return web.Response(status=200)
