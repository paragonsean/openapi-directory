from typing import List, Dict
from aiohttp import web

from openapi_server.models.operations_list_default_response import OperationsListDefaultResponse
from openapi_server.models.statistics_list_result import StatisticsListResult
from openapi_server import util


async def statistics_list_by_automation_account(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version, filter=None) -> web.Response:
    """statistics_list_by_automation_account

    Retrieve the statistics for the account.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)
