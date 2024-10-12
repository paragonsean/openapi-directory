from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.query_body import QueryBody
from openapi_server.models.query_results import QueryResults
from openapi_server import util


async def query_execute(request: web.Request, subscription_id, resource_group_name, workspace_name, api_version, body) -> web.Response:
    """Execute an Analytics query

    Executes an Analytics query for data. [Here](https://dev.loganalytics.io/documentation/Using-the-API) is an example for using POST with an Analytics query.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param workspace_name: Name of the Log Analytics workspace.
    :type workspace_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param body: The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/)
    :type body: dict | bytes

    """
    body = QueryBody.from_dict(body)
    return web.Response(status=200)


async def query_get(request: web.Request, subscription_id, resource_group_name, workspace_name, query, api_version, timespan=None) -> web.Response:
    """Execute an Analytics query

    Executes an Analytics query for data

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param workspace_name: Name of the Log Analytics workspace.
    :type workspace_name: str
    :param query: The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/)
    :type query: str
    :param api_version: Client API version.
    :type api_version: str
    :param timespan: Optional. The timespan over which to query data. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the query expression.
    :type timespan: str

    """
    return web.Response(status=200)
