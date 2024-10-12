from typing import List, Dict
from aiohttp import web

from openapi_server.models.dsc_node_configuration import DscNodeConfiguration
from openapi_server.models.dsc_node_configuration_create_or_update_parameters import DscNodeConfigurationCreateOrUpdateParameters
from openapi_server.models.dsc_node_configuration_list_by_automation_account_default_response import DscNodeConfigurationListByAutomationAccountDefaultResponse
from openapi_server.models.dsc_node_configuration_list_result import DscNodeConfigurationListResult
from openapi_server import util


async def dsc_node_configuration_create_or_update(request: web.Request, resource_group_name, automation_account_name, node_configuration_name, subscription_id, api_version, parameters) -> web.Response:
    """dsc_node_configuration_create_or_update

    Create the node configuration identified by node configuration name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param node_configuration_name: The Dsc node configuration name.
    :type node_configuration_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The create or update parameters for configuration.
    :type parameters: dict | bytes

    """
    parameters = DscNodeConfigurationCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def dsc_node_configuration_delete(request: web.Request, subscription_id, resource_group_name, automation_account_name, node_configuration_name, api_version) -> web.Response:
    """dsc_node_configuration_delete

    Delete the Dsc node configurations by node configuration.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param node_configuration_name: The Dsc node configuration name.
    :type node_configuration_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def dsc_node_configuration_get(request: web.Request, subscription_id, resource_group_name, automation_account_name, node_configuration_name, api_version) -> web.Response:
    """dsc_node_configuration_get

    Retrieve the Dsc node configurations by node configuration.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param node_configuration_name: The Dsc node configuration name.
    :type node_configuration_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def dsc_node_configuration_list_by_automation_account(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version, filter=None, skip=None, top=None, inlinecount=None) -> web.Response:
    """dsc_node_configuration_list_by_automation_account

    Retrieve a list of dsc node configurations.

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
    :param skip: The number of rows to skip.
    :type skip: int
    :param top: The number of rows to take.
    :type top: int
    :param inlinecount: Return total rows.
    :type inlinecount: str

    """
    return web.Response(status=200)
