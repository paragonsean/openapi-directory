from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.usage_details_list_result import UsageDetailsListResult
from openapi_server import util


async def usage_details_list(request: web.Request, subscription_id, api_version, expand=None, filter=None, skiptoken=None, top=None, apply=None) -> web.Response:
    """usage_details_list

    Lists the usage details for a scope by current billing period. Usage details are available via this API only for May 1, 2014 or later.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-31.
    :type api_version: str
    :param expand: May be used to expand the properties/additionalProperties or properties/meterDetails within a list of usage details. By default, these fields are not included when listing usage details.
    :type expand: str
    :param filter: May be used to filter usageDetails by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName, properties/instanceId or tags. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N usageDetails.
    :type top: int
    :param apply: OData apply expression to aggregate usageDetails by tags or (tags and properties/usageStart)
    :type apply: str

    """
    return web.Response(status=200)


async def usage_details_list_by_billing_account(request: web.Request, billing_account_id, api_version, expand=None, filter=None, skiptoken=None, top=None, apply=None) -> web.Response:
    """usage_details_list_by_billing_account

    Lists the usage details by billingAccountId for a scope by current billing period. Usage details are available via this API only for May 1, 2014 or later.

    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-31.
    :type api_version: str
    :param expand: May be used to expand the properties/additionalProperties or properties/meterDetails within a list of usage details. By default, these fields are not included when listing usage details.
    :type expand: str
    :param filter: May be used to filter usageDetails by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName, properties/instanceId or tags. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N usageDetails.
    :type top: int
    :param apply: OData apply expression to aggregate usageDetails by tags or (tags and properties/usageStart)
    :type apply: str

    """
    return web.Response(status=200)


async def usage_details_list_by_billing_period(request: web.Request, subscription_id, billing_period_name, api_version, expand=None, filter=None, apply=None, skiptoken=None, top=None) -> web.Response:
    """usage_details_list_by_billing_period

    Lists the usage details for a scope by billing period. Usage details are available via this API only for May 1, 2014 or later.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param billing_period_name: Billing Period Name.
    :type billing_period_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-31.
    :type api_version: str
    :param expand: May be used to expand the properties/additionalProperties or properties/meterDetails within a list of usage details. By default, these fields are not included when listing usage details.
    :type expand: str
    :param filter: May be used to filter usageDetails by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str
    :param apply: OData apply expression to aggregate usageDetails by tags or (tags and properties/usageStart) for specified billing period
    :type apply: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N usageDetails.
    :type top: int

    """
    return web.Response(status=200)


async def usage_details_list_by_department(request: web.Request, department_id, api_version, expand=None, filter=None, skiptoken=None, top=None, apply=None) -> web.Response:
    """usage_details_list_by_department

    Lists the usage details by departmentId for a scope by current billing period. Usage details are available via this API only for May 1, 2014 or later.

    :param department_id: Department ID
    :type department_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-31.
    :type api_version: str
    :param expand: May be used to expand the properties/additionalProperties or properties/meterDetails within a list of usage details. By default, these fields are not included when listing usage details.
    :type expand: str
    :param filter: May be used to filter usageDetails by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName, properties/instanceId or tags. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N usageDetails.
    :type top: int
    :param apply: OData apply expression to aggregate usageDetails by tags or (tags and properties/usageStart)
    :type apply: str

    """
    return web.Response(status=200)


async def usage_details_list_by_enrollment_account(request: web.Request, enrollment_account_id, api_version, expand=None, filter=None, skiptoken=None, top=None, apply=None) -> web.Response:
    """usage_details_list_by_enrollment_account

    Lists the usage details by enrollmentAccountId for a scope by current billing period. Usage details are available via this API only for May 1, 2014 or later.

    :param enrollment_account_id: EnrollmentAccount ID
    :type enrollment_account_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-31.
    :type api_version: str
    :param expand: May be used to expand the properties/additionalProperties or properties/meterDetails within a list of usage details. By default, these fields are not included when listing usage details.
    :type expand: str
    :param filter: May be used to filter usageDetails by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName, properties/instanceId or tags. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N usageDetails.
    :type top: int
    :param apply: OData apply expression to aggregate usageDetails by tags or (tags and properties/usageStart)
    :type apply: str

    """
    return web.Response(status=200)


async def usage_details_list_by_management_group(request: web.Request, management_group_id, api_version, expand=None, filter=None, skiptoken=None, top=None, apply=None) -> web.Response:
    """usage_details_list_by_management_group

    Lists the usage detail records for all subscriptions belonging to a management group scope by current billing period. Usage details are available via this API only for May 1, 2014 or later.

    :param management_group_id: Azure Management Group ID.
    :type management_group_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-31.
    :type api_version: str
    :param expand: May be used to expand the properties/additionalProperties or properties/meterDetails within a list of usage details. By default, these fields are not included when listing usage details.
    :type expand: str
    :param filter: May be used to filter usageDetails by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName, properties/instanceId or tags. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N usageDetails.
    :type top: int
    :param apply: OData apply expression to aggregate usageDetails by tags or (tags and properties/usageStart)
    :type apply: str

    """
    return web.Response(status=200)


async def usage_details_list_for_billing_period_by_billing_account(request: web.Request, billing_account_id, billing_period_name, api_version, expand=None, filter=None, apply=None, skiptoken=None, top=None) -> web.Response:
    """usage_details_list_for_billing_period_by_billing_account

    Lists the usage details based on billingAccountId for a scope by billing period. Usage details are available via this API only for May 1, 2014 or later.

    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param billing_period_name: Billing Period Name.
    :type billing_period_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-31.
    :type api_version: str
    :param expand: May be used to expand the properties/additionalProperties or properties/meterDetails within a list of usage details. By default, these fields are not included when listing usage details.
    :type expand: str
    :param filter: May be used to filter usageDetails by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str
    :param apply: OData apply expression to aggregate usageDetails by tags or (tags and properties/usageStart) for specified billing period
    :type apply: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N usageDetails.
    :type top: int

    """
    return web.Response(status=200)


async def usage_details_list_for_billing_period_by_department(request: web.Request, department_id, billing_period_name, api_version, expand=None, filter=None, apply=None, skiptoken=None, top=None) -> web.Response:
    """usage_details_list_for_billing_period_by_department

    Lists the usage details based on departmentId for a scope by billing period. Usage details are available via this API only for May 1, 2014 or later.

    :param department_id: Department ID
    :type department_id: str
    :param billing_period_name: Billing Period Name.
    :type billing_period_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-31.
    :type api_version: str
    :param expand: May be used to expand the properties/additionalProperties or properties/meterDetails within a list of usage details. By default, these fields are not included when listing usage details.
    :type expand: str
    :param filter: May be used to filter usageDetails by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str
    :param apply: OData apply expression to aggregate usageDetails by tags or (tags and properties/usageStart) for specified billing period
    :type apply: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N usageDetails.
    :type top: int

    """
    return web.Response(status=200)


async def usage_details_list_for_billing_period_by_enrollment_account(request: web.Request, enrollment_account_id, billing_period_name, api_version, expand=None, filter=None, apply=None, skiptoken=None, top=None) -> web.Response:
    """usage_details_list_for_billing_period_by_enrollment_account

    Lists the usage details based on enrollmentAccountId for a scope by billing period. Usage details are available via this API only for May 1, 2014 or later.

    :param enrollment_account_id: EnrollmentAccount ID
    :type enrollment_account_id: str
    :param billing_period_name: Billing Period Name.
    :type billing_period_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-31.
    :type api_version: str
    :param expand: May be used to expand the properties/additionalProperties or properties/meterDetails within a list of usage details. By default, these fields are not included when listing usage details.
    :type expand: str
    :param filter: May be used to filter usageDetails by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str
    :param apply: OData apply expression to aggregate usageDetails by tags or (tags and properties/usageStart) for specified billing period
    :type apply: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N usageDetails.
    :type top: int

    """
    return web.Response(status=200)


async def usage_details_list_for_billing_period_by_management_group(request: web.Request, management_group_id, billing_period_name, api_version, expand=None, filter=None, apply=None, skiptoken=None, top=None) -> web.Response:
    """usage_details_list_for_billing_period_by_management_group

    Lists the usage detail records for all subscriptions belonging to a management group scope by specified billing period. Usage details are available via this API only for May 1, 2014 or later.

    :param management_group_id: Azure Management Group ID.
    :type management_group_id: str
    :param billing_period_name: Billing Period Name.
    :type billing_period_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-31.
    :type api_version: str
    :param expand: May be used to expand the properties/additionalProperties or properties/meterDetails within a list of usage details. By default, these fields are not included when listing usage details.
    :type expand: str
    :param filter: May be used to filter usageDetails by properties/usageEnd (Utc time), properties/usageStart (Utc time), properties/resourceGroup, properties/instanceName or properties/instanceId. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str
    :param apply: OData apply expression to aggregate usageDetails by tags or (tags and properties/usageStart) for specified billing period
    :type apply: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N usageDetails.
    :type top: int

    """
    return web.Response(status=200)
