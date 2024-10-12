from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.management_group_aggregated_cost_result import ManagementGroupAggregatedCostResult
from openapi_server import util


async def aggregated_cost_get_by_management_group(request: web.Request, management_group_id, api_version) -> web.Response:
    """aggregated_cost_get_by_management_group

    Provides the aggregate cost of a management group and all child management groups by current billing period.

    :param management_group_id: Azure Management Group ID.
    :type management_group_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-06-30.
    :type api_version: str

    """
    return web.Response(status=200)


async def aggregated_cost_get_for_billing_period_by_management_group(request: web.Request, management_group_id, billing_period_name, api_version) -> web.Response:
    """aggregated_cost_get_for_billing_period_by_management_group

    Provides the aggregate cost of a management group and all child management groups by specified billing period

    :param management_group_id: Azure Management Group ID.
    :type management_group_id: str
    :param billing_period_name: Billing Period Name.
    :type billing_period_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-06-30.
    :type api_version: str

    """
    return web.Response(status=200)
