from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.query_result import QueryResult
from openapi_server.models.report_config_definition import ReportConfigDefinition
from openapi_server import util


async def query_billing_account(request: web.Request, api_version, billing_account_id, parameters) -> web.Response:
    """query_billing_account

    Lists the usage data for billing account.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-05-31.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param parameters: Parameters supplied to the CreateOrUpdate Report Config operation.
    :type parameters: dict | bytes

    """
    parameters = ReportConfigDefinition.from_dict(parameters)
    return web.Response(status=200)


async def query_resource_group(request: web.Request, api_version, subscription_id, resource_group_name, parameters) -> web.Response:
    """query_resource_group

    Lists the usage data for subscriptionId and resource group.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-05-31.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Azure Resource Group Name.
    :type resource_group_name: str
    :param parameters: Parameters supplied to the CreateOrUpdate Report Config operation.
    :type parameters: dict | bytes

    """
    parameters = ReportConfigDefinition.from_dict(parameters)
    return web.Response(status=200)


async def query_subscription(request: web.Request, api_version, subscription_id, parameters) -> web.Response:
    """query_subscription

    Lists the usage data for subscriptionId.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-05-31.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param parameters: Parameters supplied to the CreateOrUpdate Report Config operation.
    :type parameters: dict | bytes

    """
    parameters = ReportConfigDefinition.from_dict(parameters)
    return web.Response(status=200)
