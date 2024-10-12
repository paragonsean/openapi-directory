from typing import List, Dict
from aiohttp import web

from openapi_server.models.budget import Budget
from openapi_server.models.budgets_list_result import BudgetsListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def budgets_create_or_update(request: web.Request, scope, api_version, budget_name, parameters) -> web.Response:
    """budgets_create_or_update

    The operation to create or update a budget. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

    :param scope: The scope associated with budget operations. This includes &#39;/subscriptions/{subscriptionId}/&#39; for subscription scope, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope, &#39;/providers/Microsoft.Management/managementGroups/{managementGroupId}&#39; for Management Group scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for billingProfile scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}&#39; for invoiceSection scope.
    :type scope: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-05-01.
    :type api_version: str
    :param budget_name: Budget Name.
    :type budget_name: str
    :param parameters: Parameters supplied to the Create Budget operation.
    :type parameters: dict | bytes

    """
    parameters = Budget.from_dict(parameters)
    return web.Response(status=200)


async def budgets_delete(request: web.Request, scope, api_version, budget_name) -> web.Response:
    """budgets_delete

    The operation to delete a budget.

    :param scope: The scope associated with budget operations. This includes &#39;/subscriptions/{subscriptionId}/&#39; for subscription scope, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope, &#39;/providers/Microsoft.Management/managementGroups/{managementGroupId}&#39; for Management Group scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for billingProfile scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}&#39; for invoiceSection scope.
    :type scope: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-05-01.
    :type api_version: str
    :param budget_name: Budget Name.
    :type budget_name: str

    """
    return web.Response(status=200)


async def budgets_get(request: web.Request, scope, api_version, budget_name) -> web.Response:
    """budgets_get

    Gets the budget for the scope by budget name.

    :param scope: The scope associated with budget operations. This includes &#39;/subscriptions/{subscriptionId}/&#39; for subscription scope, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope, &#39;/providers/Microsoft.Management/managementGroups/{managementGroupId}&#39; for Management Group scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for billingProfile scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}&#39; for invoiceSection scope.
    :type scope: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-05-01.
    :type api_version: str
    :param budget_name: Budget Name.
    :type budget_name: str

    """
    return web.Response(status=200)


async def budgets_list(request: web.Request, scope, api_version) -> web.Response:
    """budgets_list

    Lists all budgets for the defined scope.

    :param scope: The scope associated with budget operations. This includes &#39;/subscriptions/{subscriptionId}/&#39; for subscription scope, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope, &#39;/providers/Microsoft.Management/managementGroups/{managementGroupId}&#39; for Management Group scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for billingProfile scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}&#39; for invoiceSection scope.
    :type scope: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-05-01.
    :type api_version: str

    """
    return web.Response(status=200)
