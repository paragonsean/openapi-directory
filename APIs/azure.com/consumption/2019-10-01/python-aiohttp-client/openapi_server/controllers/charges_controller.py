from typing import List, Dict
from aiohttp import web

from openapi_server.models.charges_list_result import ChargesListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def charges_list(request: web.Request, scope, api_version, start_date=None, end_date=None, filter=None, apply=None) -> web.Response:
    """charges_list

    Lists the charges based for the defined scope.

    :param scope: The scope associated with charges operations. This includes &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, and &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope. For department and enrollment accounts, you can also add billing period to the scope using &#39;/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}&#39;. For e.g. to specify billing period at department scope use &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}&#39;. Also, Modern Commerce Account scopes are &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for billingAccount scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for billingProfile scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}&#39; for invoiceSection scope, and &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}&#39; specific for partners.
    :type scope: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01.
    :type api_version: str
    :param start_date: Start date
    :type start_date: str
    :param end_date: End date
    :type end_date: str
    :param filter: May be used to filter charges by properties/usageEnd (Utc time), properties/usageStart (Utc time). The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str
    :param apply: May be used to group charges for billingAccount scope by properties/billingProfileId, properties/invoiceSectionId, properties/customerId (specific for Partner Led), or for billingProfile scope by properties/invoiceSectionId.
    :type apply: str

    """
    return web.Response(status=200)
