from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.export import Export
from openapi_server.models.export_execution_list_result import ExportExecutionListResult
from openapi_server.models.export_list_result import ExportListResult
from openapi_server import util


async def exports_create_or_update(request: web.Request, scope, api_version, export_name, parameters) -> web.Response:
    """exports_create_or_update

    The operation to create or update a export. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

    :param scope: The scope associated with export operations. This includes &#39;/subscriptions/{subscriptionId}&#39; for subscription scope, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope and &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope.
    :type scope: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-05-31.
    :type api_version: str
    :param export_name: Export Name.
    :type export_name: str
    :param parameters: Parameters supplied to the CreateOrUpdate Export operation.
    :type parameters: dict | bytes

    """
    parameters = Export.from_dict(parameters)
    return web.Response(status=200)


async def exports_delete(request: web.Request, scope, api_version, export_name) -> web.Response:
    """exports_delete

    The operation to delete a export.

    :param scope: The scope associated with export operations. This includes &#39;/subscriptions/{subscriptionId}&#39; for subscription scope, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope and &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope.
    :type scope: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-05-31.
    :type api_version: str
    :param export_name: Export Name.
    :type export_name: str

    """
    return web.Response(status=200)


async def exports_execute(request: web.Request, scope, api_version, export_name) -> web.Response:
    """exports_execute

    The operation to execute a export.

    :param scope: The scope associated with export operations. This includes &#39;/subscriptions/{subscriptionId}&#39; for subscription scope, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope and &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope.
    :type scope: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-05-31.
    :type api_version: str
    :param export_name: Export Name.
    :type export_name: str

    """
    return web.Response(status=200)


async def exports_get(request: web.Request, scope, api_version, export_name) -> web.Response:
    """exports_get

    Gets the export for the defined scope by export name.

    :param scope: The scope associated with export operations. This includes &#39;/subscriptions/{subscriptionId}&#39; for subscription scope, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope and &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope.
    :type scope: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-05-31.
    :type api_version: str
    :param export_name: Export Name.
    :type export_name: str

    """
    return web.Response(status=200)


async def exports_get_execution_history(request: web.Request, scope, api_version, export_name) -> web.Response:
    """exports_get_execution_history

    Gets the execution history of a export for the defined scope by export name.

    :param scope: The scope associated with export operations. This includes &#39;/subscriptions/{subscriptionId}&#39; for subscription scope, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope and &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope.
    :type scope: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-05-31.
    :type api_version: str
    :param export_name: Export Name.
    :type export_name: str

    """
    return web.Response(status=200)


async def exports_list(request: web.Request, scope, api_version) -> web.Response:
    """exports_list

    Lists all exports at the given scope.

    :param scope: The scope associated with export operations. This includes &#39;/subscriptions/{subscriptionId}&#39; for subscription scope, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope and &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope.
    :type scope: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-05-31.
    :type api_version: str

    """
    return web.Response(status=200)
