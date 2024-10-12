from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.query_definition import QueryDefinition
from openapi_server.models.query_result import QueryResult
from openapi_server import util


async def query_usage(request: web.Request, scope, api_version, parameters) -> web.Response:
    """query_usage

    Query the usage data for scope defined.

    :param scope: The scope associated with query and export operations. This includes &#39;/subscriptions/{subscriptionId}/&#39; for subscription scope, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope and &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope, &#39;/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for billingProfile scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}&#39; for invoiceSection scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}&#39; specific for partners, &#39;providers/Microsoft.CostManagement/ExternalSubscriptions/{externalSubscriptionId}&#39; for linked account and &#39;providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountId}&#39; for consolidated account
    :type scope: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01.
    :type api_version: str
    :param parameters: Parameters supplied to the CreateOrUpdate Query Config operation.
    :type parameters: dict | bytes

    """
    parameters = QueryDefinition.from_dict(parameters)
    return web.Response(status=200)
