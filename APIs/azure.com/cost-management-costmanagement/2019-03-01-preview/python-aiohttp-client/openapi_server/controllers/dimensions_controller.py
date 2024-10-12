from typing import List, Dict
from aiohttp import web

from openapi_server.models.dimensions_list_result import DimensionsListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def dimensions_list_by_billing_account(request: web.Request, api_version, billing_account_id, filter=None, expand=None, skiptoken=None, top=None) -> web.Response:
    """dimensions_list_by_billing_account

    Lists the dimensions by billingAccount Id.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-03-01-preview
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param filter: May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;.
    :type filter: str
    :param expand: May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions.
    :type expand: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N dimension data.
    :type top: int

    """
    return web.Response(status=200)


async def dimensions_list_by_department(request: web.Request, api_version, billing_account_id, department_id, filter=None, expand=None, skiptoken=None, top=None) -> web.Response:
    """dimensions_list_by_department

    Lists the dimensions by Department Id.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-03-01-preview
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param department_id: Department ID
    :type department_id: str
    :param filter: May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;.
    :type filter: str
    :param expand: May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions.
    :type expand: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N dimension data.
    :type top: int

    """
    return web.Response(status=200)


async def dimensions_list_by_enrollment_account(request: web.Request, api_version, billing_account_id, enrollment_account_id, filter=None, expand=None, skiptoken=None, top=None) -> web.Response:
    """dimensions_list_by_enrollment_account

    Lists the dimensions by Enrollment Account Id.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-03-01-preview
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param enrollment_account_id: Enrollment Account ID
    :type enrollment_account_id: str
    :param filter: May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;.
    :type filter: str
    :param expand: May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions.
    :type expand: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N dimension data.
    :type top: int

    """
    return web.Response(status=200)


async def dimensions_list_by_management_group(request: web.Request, api_version, management_group_id, filter=None, expand=None, skiptoken=None, top=None) -> web.Response:
    """dimensions_list_by_management_group

    Lists the dimensions by managementGroup Id.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-03-01-preview
    :type api_version: str
    :param management_group_id: ManagementGroup ID
    :type management_group_id: str
    :param filter: May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;.
    :type filter: str
    :param expand: May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions.
    :type expand: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N dimension data.
    :type top: int

    """
    return web.Response(status=200)


async def dimensions_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name, filter=None, expand=None, skiptoken=None, top=None) -> web.Response:
    """dimensions_list_by_resource_group

    Lists the dimensions by resource group Id.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-03-01-preview
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Azure Resource Group Name.
    :type resource_group_name: str
    :param filter: May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;.
    :type filter: str
    :param expand: May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions.
    :type expand: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N dimension data.
    :type top: int

    """
    return web.Response(status=200)


async def dimensions_list_by_subscription(request: web.Request, api_version, subscription_id, filter=None, expand=None, skiptoken=None, top=None) -> web.Response:
    """dimensions_list_by_subscription

    Lists the dimensions by subscription Id.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-03-01-preview
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param filter: May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;.
    :type filter: str
    :param expand: May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions.
    :type expand: str
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: May be used to limit the number of results to the most recent N dimension data.
    :type top: int

    """
    return web.Response(status=200)
