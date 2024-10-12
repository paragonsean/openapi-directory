from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.report import Report
from openapi_server.models.report_execution_list_result import ReportExecutionListResult
from openapi_server.models.report_list_result import ReportListResult
from openapi_server import util


async def reports_create_or_update(request: web.Request, api_version, subscription_id, report_name, parameters) -> web.Response:
    """reports_create_or_update

    The operation to create or update a report. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param report_name: Report Name.
    :type report_name: str
    :param parameters: Parameters supplied to the CreateOrUpdate Report operation.
    :type parameters: dict | bytes

    """
    parameters = Report.from_dict(parameters)
    return web.Response(status=200)


async def reports_create_or_update_by_billing_account(request: web.Request, api_version, billing_account_id, report_name, parameters) -> web.Response:
    """reports_create_or_update_by_billing_account

    The operation to create or update a report for billingAccount. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param report_name: Report Name.
    :type report_name: str
    :param parameters: Parameters supplied to the CreateOrUpdate Report operation.
    :type parameters: dict | bytes

    """
    parameters = Report.from_dict(parameters)
    return web.Response(status=200)


async def reports_create_or_update_by_department(request: web.Request, api_version, department_id, report_name, parameters) -> web.Response:
    """reports_create_or_update_by_department

    The operation to create or update a report for department. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param department_id: Department ID
    :type department_id: str
    :param report_name: Report Name.
    :type report_name: str
    :param parameters: Parameters supplied to the CreateOrUpdate Report operation.
    :type parameters: dict | bytes

    """
    parameters = Report.from_dict(parameters)
    return web.Response(status=200)


async def reports_create_or_update_by_resource_group_name(request: web.Request, api_version, subscription_id, resource_group_name, report_name, parameters) -> web.Response:
    """reports_create_or_update_by_resource_group_name

    The operation to create or update a report. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Azure Resource Group Name.
    :type resource_group_name: str
    :param report_name: Report Name.
    :type report_name: str
    :param parameters: Parameters supplied to the CreateOrUpdate Report operation.
    :type parameters: dict | bytes

    """
    parameters = Report.from_dict(parameters)
    return web.Response(status=200)


async def reports_delete(request: web.Request, api_version, subscription_id, report_name) -> web.Response:
    """reports_delete

    The operation to delete a report.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param report_name: Report Name.
    :type report_name: str

    """
    return web.Response(status=200)


async def reports_delete_by_billing_account(request: web.Request, api_version, billing_account_id, report_name) -> web.Response:
    """reports_delete_by_billing_account

    The operation to delete a report for billing account.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param report_name: Report Name.
    :type report_name: str

    """
    return web.Response(status=200)


async def reports_delete_by_department(request: web.Request, api_version, department_id, report_name) -> web.Response:
    """reports_delete_by_department

    The operation to delete a report for department.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param department_id: Department ID
    :type department_id: str
    :param report_name: Report Name.
    :type report_name: str

    """
    return web.Response(status=200)


async def reports_delete_by_resource_group_name(request: web.Request, api_version, subscription_id, resource_group_name, report_name) -> web.Response:
    """reports_delete_by_resource_group_name

    The operation to delete a report.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Azure Resource Group Name.
    :type resource_group_name: str
    :param report_name: Report Name.
    :type report_name: str

    """
    return web.Response(status=200)


async def reports_execute(request: web.Request, api_version, subscription_id, report_name) -> web.Response:
    """reports_execute

    The operation to execute a report.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param report_name: Report Name.
    :type report_name: str

    """
    return web.Response(status=200)


async def reports_execute_by_billing_account(request: web.Request, api_version, billing_account_id, report_name) -> web.Response:
    """reports_execute_by_billing_account

    The operation to execute a report by billing account.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param report_name: Report Name.
    :type report_name: str

    """
    return web.Response(status=200)


async def reports_execute_by_department(request: web.Request, api_version, department_id, report_name) -> web.Response:
    """reports_execute_by_department

    The operation to execute a report by department.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param department_id: Department ID
    :type department_id: str
    :param report_name: Report Name.
    :type report_name: str

    """
    return web.Response(status=200)


async def reports_execute_by_resource_group_name(request: web.Request, api_version, subscription_id, resource_group_name, report_name) -> web.Response:
    """reports_execute_by_resource_group_name

    The operation to execute a report.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Azure Resource Group Name.
    :type resource_group_name: str
    :param report_name: Report Name.
    :type report_name: str

    """
    return web.Response(status=200)


async def reports_get(request: web.Request, api_version, subscription_id, report_name) -> web.Response:
    """reports_get

    Gets the report for a subscription by report name.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param report_name: Report Name.
    :type report_name: str

    """
    return web.Response(status=200)


async def reports_get_by_billing_account(request: web.Request, api_version, billing_account_id, report_name) -> web.Response:
    """reports_get_by_billing_account

    Gets the report for a billing account by report name.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param report_name: Report Name.
    :type report_name: str

    """
    return web.Response(status=200)


async def reports_get_by_department(request: web.Request, api_version, department_id, report_name) -> web.Response:
    """reports_get_by_department

    Gets the report for a department by report name.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param department_id: Department ID
    :type department_id: str
    :param report_name: Report Name.
    :type report_name: str

    """
    return web.Response(status=200)


async def reports_get_by_resource_group_name(request: web.Request, api_version, subscription_id, resource_group_name, report_name) -> web.Response:
    """reports_get_by_resource_group_name

    Gets the report for a resource group under a subscription by report name.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Azure Resource Group Name.
    :type resource_group_name: str
    :param report_name: Report Name.
    :type report_name: str

    """
    return web.Response(status=200)


async def reports_get_execution_history(request: web.Request, api_version, subscription_id, report_name) -> web.Response:
    """reports_get_execution_history

    Gets the execution history of a report for a subscription by report name.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param report_name: Report Name.
    :type report_name: str

    """
    return web.Response(status=200)


async def reports_get_execution_history_by_billing_account(request: web.Request, api_version, billing_account_id, report_name) -> web.Response:
    """reports_get_execution_history_by_billing_account

    Gets the execution history of a report for a billing account by report name.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param report_name: Report Name.
    :type report_name: str

    """
    return web.Response(status=200)


async def reports_get_execution_history_by_department(request: web.Request, api_version, department_id, report_name) -> web.Response:
    """reports_get_execution_history_by_department

    Gets the execution history of a report for a department by report name.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param department_id: Department ID
    :type department_id: str
    :param report_name: Report Name.
    :type report_name: str

    """
    return web.Response(status=200)


async def reports_get_execution_history_by_resource_group_name(request: web.Request, api_version, subscription_id, resource_group_name, report_name) -> web.Response:
    """reports_get_execution_history_by_resource_group_name

    Gets the execution history of a report for a resource group by report name.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Azure Resource Group Name.
    :type resource_group_name: str
    :param report_name: Report Name.
    :type report_name: str

    """
    return web.Response(status=200)


async def reports_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """reports_list

    Lists all reports for a subscription.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def reports_list_by_billing_account(request: web.Request, api_version, billing_account_id) -> web.Response:
    """reports_list_by_billing_account

    Lists all reports for a billing account.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str

    """
    return web.Response(status=200)


async def reports_list_by_department(request: web.Request, api_version, department_id) -> web.Response:
    """reports_list_by_department

    Lists all reports for a department.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param department_id: Department ID
    :type department_id: str

    """
    return web.Response(status=200)


async def reports_list_by_resource_group_name(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """reports_list_by_resource_group_name

    Lists all reports for a resource group under a subscription.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-08-01-preview.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Azure Resource Group Name.
    :type resource_group_name: str

    """
    return web.Response(status=200)
