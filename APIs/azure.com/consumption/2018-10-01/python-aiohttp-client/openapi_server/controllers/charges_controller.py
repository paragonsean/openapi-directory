from typing import List, Dict
from aiohttp import web

from openapi_server.models.charge_summary import ChargeSummary
from openapi_server.models.charges_list_result import ChargesListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def charges_list_by_department(request: web.Request, billing_account_id, department_id, api_version, filter=None) -> web.Response:
    """charges_list_by_department

    Lists the charges by departmentId.

    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param department_id: Department ID
    :type department_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-10-01.
    :type api_version: str
    :param filter: May be used to filter charges by properties/usageEnd (Utc time), properties/usageStart (Utc time). The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str

    """
    return web.Response(status=200)


async def charges_list_by_enrollment_account(request: web.Request, billing_account_id, enrollment_account_id, api_version, filter=None) -> web.Response:
    """charges_list_by_enrollment_account

    Lists the charges by enrollmentAccountId.

    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param enrollment_account_id: EnrollmentAccount ID
    :type enrollment_account_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-10-01.
    :type api_version: str
    :param filter: May be used to filter charges by properties/usageEnd (Utc time), properties/usageStart (Utc time). The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str

    """
    return web.Response(status=200)


async def charges_list_for_billing_period_by_department(request: web.Request, billing_account_id, department_id, billing_period_name, api_version, filter=None) -> web.Response:
    """charges_list_for_billing_period_by_department

    Lists the charges based on departmentId by billing period.

    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param department_id: Department ID
    :type department_id: str
    :param billing_period_name: Billing Period Name.
    :type billing_period_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-10-01.
    :type api_version: str
    :param filter: May be used to filter charges by properties/usageEnd (Utc time), properties/usageStart (Utc time). The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str

    """
    return web.Response(status=200)


async def charges_list_for_billing_period_by_enrollment_account(request: web.Request, billing_account_id, enrollment_account_id, billing_period_name, api_version, filter=None) -> web.Response:
    """charges_list_for_billing_period_by_enrollment_account

    Lists the charges based on enrollmentAccountId by billing period.

    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param enrollment_account_id: EnrollmentAccount ID
    :type enrollment_account_id: str
    :param billing_period_name: Billing Period Name.
    :type billing_period_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-10-01.
    :type api_version: str
    :param filter: May be used to filter charges by properties/usageEnd (Utc time), properties/usageStart (Utc time). The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str

    """
    return web.Response(status=200)
