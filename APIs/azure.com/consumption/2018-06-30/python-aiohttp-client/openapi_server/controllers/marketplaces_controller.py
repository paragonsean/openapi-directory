from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.marketplaces_list_result import MarketplacesListResult
from openapi_server import util


async def marketplaces_list(request: web.Request, api_version, subscription_id, filter=None, top=None, skiptoken=None) -> web.Response:
    """marketplaces_list

    Lists the marketplaces for a scope by subscriptionId and current billing period. Marketplaces are available via this API only for May 1, 2014 or later.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-06-30.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param filter: May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;.
    :type filter: str
    :param top: May be used to limit the number of results to the most recent N marketplaces.
    :type top: int
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str

    """
    return web.Response(status=200)


async def marketplaces_list_by_billing_account(request: web.Request, api_version, billing_account_id, filter=None, top=None, skiptoken=None) -> web.Response:
    """marketplaces_list_by_billing_account

    Lists the marketplaces for a scope by billingAccountId and current billing period. Marketplaces are available via this API only for May 1, 2014 or later.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-06-30.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param filter: May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;.
    :type filter: str
    :param top: May be used to limit the number of results to the most recent N marketplaces.
    :type top: int
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str

    """
    return web.Response(status=200)


async def marketplaces_list_by_billing_period(request: web.Request, api_version, subscription_id, billing_period_name, filter=None, top=None, skiptoken=None) -> web.Response:
    """marketplaces_list_by_billing_period

    Lists the marketplaces for a scope by billing period and subscriptionId. Marketplaces are available via this API only for May 1, 2014 or later.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-06-30.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param billing_period_name: Billing Period Name.
    :type billing_period_name: str
    :param filter: May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;.
    :type filter: str
    :param top: May be used to limit the number of results to the most recent N marketplaces.
    :type top: int
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str

    """
    return web.Response(status=200)


async def marketplaces_list_by_department(request: web.Request, api_version, department_id, filter=None, top=None, skiptoken=None) -> web.Response:
    """marketplaces_list_by_department

    Lists the marketplaces for a scope by departmentId and current billing period. Marketplaces are available via this API only for May 1, 2014 or later.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-06-30.
    :type api_version: str
    :param department_id: Department ID
    :type department_id: str
    :param filter: May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;.
    :type filter: str
    :param top: May be used to limit the number of results to the most recent N marketplaces.
    :type top: int
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str

    """
    return web.Response(status=200)


async def marketplaces_list_by_enrollment_account(request: web.Request, api_version, enrollment_account_id, filter=None, top=None, skiptoken=None) -> web.Response:
    """marketplaces_list_by_enrollment_account

    Lists the marketplaces for a scope by enrollmentAccountId and current billing period. Marketplaces are available via this API only for May 1, 2014 or later.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-06-30.
    :type api_version: str
    :param enrollment_account_id: EnrollmentAccount ID
    :type enrollment_account_id: str
    :param filter: May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;.
    :type filter: str
    :param top: May be used to limit the number of results to the most recent N marketplaces.
    :type top: int
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str

    """
    return web.Response(status=200)


async def marketplaces_list_for_billing_period_by_billing_account(request: web.Request, api_version, billing_account_id, billing_period_name, filter=None, top=None, skiptoken=None) -> web.Response:
    """marketplaces_list_for_billing_period_by_billing_account

    Lists the marketplaces for a scope by billing period and billingAccountId. Marketplaces are available via this API only for May 1, 2014 or later.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-06-30.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param billing_period_name: Billing Period Name.
    :type billing_period_name: str
    :param filter: May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;.
    :type filter: str
    :param top: May be used to limit the number of results to the most recent N marketplaces.
    :type top: int
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str

    """
    return web.Response(status=200)


async def marketplaces_list_for_billing_period_by_department(request: web.Request, api_version, department_id, billing_period_name, filter=None, top=None, skiptoken=None) -> web.Response:
    """marketplaces_list_for_billing_period_by_department

    Lists the marketplaces for a scope by billing period and departmentId. Marketplaces are available via this API only for May 1, 2014 or later.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-06-30.
    :type api_version: str
    :param department_id: Department ID
    :type department_id: str
    :param billing_period_name: Billing Period Name.
    :type billing_period_name: str
    :param filter: May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;.
    :type filter: str
    :param top: May be used to limit the number of results to the most recent N marketplaces.
    :type top: int
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str

    """
    return web.Response(status=200)


async def marketplaces_list_for_billing_period_by_enrollment_account(request: web.Request, api_version, enrollment_account_id, billing_period_name, filter=None, top=None, skiptoken=None) -> web.Response:
    """marketplaces_list_for_billing_period_by_enrollment_account

    Lists the marketplaces for a scope by billing period and enrollmentAccountId. Marketplaces are available via this API only for May 1, 2014 or later.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-06-30.
    :type api_version: str
    :param enrollment_account_id: EnrollmentAccount ID
    :type enrollment_account_id: str
    :param billing_period_name: Billing Period Name.
    :type billing_period_name: str
    :param filter: May be used to filter marketplaces by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;.
    :type filter: str
    :param top: May be used to limit the number of results to the most recent N marketplaces.
    :type top: int
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str

    """
    return web.Response(status=200)
