from typing import List, Dict
from aiohttp import web

from openapi_server.models.dimensions_list_result import DimensionsListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def dimensions_list(request: web.Request, scope, api_version, filter=None, expand=None, skiptoken=None, top=None) -> web.Response:
    """dimensions_list

    Lists the dimensions by the defined scope.

    :param scope: The scope associated with dimension operations. This includes &#39;/subscriptions/{subscriptionId}/&#39; for subscription scope, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope, &#39;/providers/Microsoft.Management/managementGroups/{managementGroupId}&#39; for Management Group scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for billingProfile scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}&#39; for invoiceSection scope, and &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}&#39; specific for partners.
    :type scope: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-11-01.
    :type api_version: str
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
