from typing import List, Dict
from aiohttp import web

from openapi_server.models.agent_registration_information_get_default_response import AgentRegistrationInformationGetDefaultResponse
from openapi_server.models.dsc_node import DscNode
from openapi_server.models.dsc_node_list_result import DscNodeListResult
from openapi_server.models.dsc_node_update_parameters import DscNodeUpdateParameters
from openapi_server import util


async def dsc_node_delete(request: web.Request, resource_group_name, automation_account_name, node_id, subscription_id, api_version) -> web.Response:
    """dsc_node_delete

    Delete the dsc node identified by node id.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param node_id: The node id.
    :type node_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def dsc_node_get(request: web.Request, resource_group_name, automation_account_name, node_id, subscription_id, api_version) -> web.Response:
    """dsc_node_get

    Retrieve the dsc node identified by node id.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param node_id: The node id.
    :type node_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def dsc_node_list_by_automation_account(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version, filter=None) -> web.Response:
    """dsc_node_list_by_automation_account

    Retrieve a list of dsc nodes.

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


async def dsc_node_update(request: web.Request, resource_group_name, automation_account_name, node_id, subscription_id, api_version, parameters) -> web.Response:
    """dsc_node_update

    Update the dsc node.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param node_id: Parameters supplied to the update dsc node.
    :type node_id: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to the update dsc node.
    :type parameters: dict | bytes

    """
    parameters = DscNodeUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
