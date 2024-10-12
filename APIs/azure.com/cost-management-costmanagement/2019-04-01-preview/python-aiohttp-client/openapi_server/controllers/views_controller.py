from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.view import View
from openapi_server.models.view_list_result import ViewListResult
from openapi_server import util


async def views_create_or_update(request: web.Request, api_version, view_name, parameters) -> web.Response:
    """views_create_or_update

    The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-04-01-preview
    :type api_version: str
    :param view_name: View name
    :type view_name: str
    :param parameters: Parameters supplied to the CreateOrUpdate View operation.
    :type parameters: dict | bytes

    """
    parameters = View.from_dict(parameters)
    return web.Response(status=200)


async def views_create_or_update_by_scope(request: web.Request, scope, api_version, view_name, parameters) -> web.Response:
    """views_create_or_update_by_scope

    The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

    :param scope: The scope associated with view operations. This includes &#39;subscriptions/{subscriptionId}&#39; for subscription scope, &#39;subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for BillingProfile scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}&#39; for InvoiceSection scope, &#39;providers/Microsoft.Management/managementGroups/{managementGroupId}&#39; for Management Group scope, &#39;providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}&#39; for External Billing Account scope and &#39;providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}&#39; for External Subscription scope.
    :type scope: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-04-01-preview
    :type api_version: str
    :param view_name: View name
    :type view_name: str
    :param parameters: Parameters supplied to the CreateOrUpdate View operation.
    :type parameters: dict | bytes

    """
    parameters = View.from_dict(parameters)
    return web.Response(status=200)


async def views_delete(request: web.Request, api_version, view_name) -> web.Response:
    """views_delete

    The operation to delete a view.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-04-01-preview
    :type api_version: str
    :param view_name: View name
    :type view_name: str

    """
    return web.Response(status=200)


async def views_delete_by_scope(request: web.Request, scope, api_version, view_name) -> web.Response:
    """views_delete_by_scope

    The operation to delete a view.

    :param scope: The scope associated with view operations. This includes &#39;subscriptions/{subscriptionId}&#39; for subscription scope, &#39;subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for BillingProfile scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}&#39; for InvoiceSection scope, &#39;providers/Microsoft.Management/managementGroups/{managementGroupId}&#39; for Management Group scope, &#39;providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}&#39; for External Billing Account scope and &#39;providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}&#39; for External Subscription scope.
    :type scope: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-04-01-preview
    :type api_version: str
    :param view_name: View name
    :type view_name: str

    """
    return web.Response(status=200)


async def views_get(request: web.Request, api_version, view_name) -> web.Response:
    """views_get

    Gets the view by view name.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-04-01-preview
    :type api_version: str
    :param view_name: View name
    :type view_name: str

    """
    return web.Response(status=200)


async def views_get_by_scope(request: web.Request, scope, api_version, view_name) -> web.Response:
    """views_get_by_scope

    Gets the view for the defined scope by view name.

    :param scope: The scope associated with view operations. This includes &#39;subscriptions/{subscriptionId}&#39; for subscription scope, &#39;subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for BillingProfile scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}&#39; for InvoiceSection scope, &#39;providers/Microsoft.Management/managementGroups/{managementGroupId}&#39; for Management Group scope, &#39;providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}&#39; for External Billing Account scope and &#39;providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}&#39; for External Subscription scope.
    :type scope: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-04-01-preview
    :type api_version: str
    :param view_name: View name
    :type view_name: str

    """
    return web.Response(status=200)


async def views_list(request: web.Request, api_version) -> web.Response:
    """views_list

    Lists all views by tenant and object.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-04-01-preview
    :type api_version: str

    """
    return web.Response(status=200)


async def views_list_by_scope(request: web.Request, scope, api_version) -> web.Response:
    """views_list_by_scope

    Lists all views at the given scope.

    :param scope: The scope associated with view operations. This includes &#39;subscriptions/{subscriptionId}&#39; for subscription scope, &#39;subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for BillingProfile scope, &#39;providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}&#39; for InvoiceSection scope, &#39;providers/Microsoft.Management/managementGroups/{managementGroupId}&#39; for Management Group scope, &#39;providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}&#39; for External Billing Account scope and &#39;providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}&#39; for External Subscription scope.
    :type scope: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-04-01-preview
    :type api_version: str

    """
    return web.Response(status=200)
