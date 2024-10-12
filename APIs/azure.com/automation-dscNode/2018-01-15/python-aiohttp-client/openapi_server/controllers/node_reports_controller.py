from typing import List, Dict
from aiohttp import web

from openapi_server.models.agent_registration_information_get_default_response import AgentRegistrationInformationGetDefaultResponse
from openapi_server.models.dsc_node_report import DscNodeReport
from openapi_server.models.dsc_node_report_list_result import DscNodeReportListResult
from openapi_server import util


async def node_reports_get(request: web.Request, resource_group_name, automation_account_name, node_id, report_id, subscription_id, api_version) -> web.Response:
    """node_reports_get

    Retrieve the Dsc node report data by node id and report id.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param node_id: The Dsc node id.
    :type node_id: str
    :param report_id: The report id.
    :type report_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def node_reports_get_content(request: web.Request, resource_group_name, automation_account_name, node_id, report_id, subscription_id, api_version) -> web.Response:
    """node_reports_get_content

    Retrieve the Dsc node reports by node id and report id.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param node_id: The Dsc node id.
    :type node_id: str
    :param report_id: The report id.
    :type report_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def node_reports_list_by_node(request: web.Request, resource_group_name, automation_account_name, node_id, subscription_id, api_version, filter=None) -> web.Response:
    """node_reports_list_by_node

    Retrieve the Dsc node report list by node id.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param node_id: The parameters supplied to the list operation.
    :type node_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)
