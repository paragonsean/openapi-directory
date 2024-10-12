from typing import List, Dict
from aiohttp import web

from openapi_server.models.dsc_configuration import DscConfiguration
from openapi_server.models.dsc_configuration_create_or_update_parameters import DscConfigurationCreateOrUpdateParameters
from openapi_server.models.dsc_configuration_list_by_automation_account_default_response import DscConfigurationListByAutomationAccountDefaultResponse
from openapi_server.models.dsc_configuration_list_result import DscConfigurationListResult
from openapi_server.models.dsc_configuration_update_parameters import DscConfigurationUpdateParameters
from openapi_server import util


async def dsc_configuration_create_or_update(request: web.Request, resource_group_name, automation_account_name, configuration_name, subscription_id, api_version, parameters) -> web.Response:
    """dsc_configuration_create_or_update

    Create the configuration identified by configuration name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param configuration_name: The create or update parameters for configuration.
    :type configuration_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The create or update parameters for configuration.
    :type parameters: dict | bytes

    """
    parameters = DscConfigurationCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def dsc_configuration_delete(request: web.Request, resource_group_name, automation_account_name, configuration_name, subscription_id, api_version) -> web.Response:
    """dsc_configuration_delete

    Delete the dsc configuration identified by configuration name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param configuration_name: The configuration name.
    :type configuration_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def dsc_configuration_get(request: web.Request, resource_group_name, automation_account_name, configuration_name, subscription_id, api_version) -> web.Response:
    """dsc_configuration_get

    Retrieve the configuration identified by configuration name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param configuration_name: The configuration name.
    :type configuration_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def dsc_configuration_get_content(request: web.Request, resource_group_name, automation_account_name, configuration_name, subscription_id, api_version) -> web.Response:
    """dsc_configuration_get_content

    Retrieve the configuration script identified by configuration name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param configuration_name: The configuration name.
    :type configuration_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def dsc_configuration_list_by_automation_account(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version, filter=None, skip=None, top=None, inlinecount=None) -> web.Response:
    """dsc_configuration_list_by_automation_account

    Retrieve a list of configurations.

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


async def dsc_configuration_update(request: web.Request, resource_group_name, automation_account_name, configuration_name, subscription_id, api_version, parameters=None) -> web.Response:
    """dsc_configuration_update

    Create the configuration identified by configuration name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param configuration_name: The create or update parameters for configuration.
    :type configuration_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The create or update parameters for configuration.
    :type parameters: dict | bytes

    """
    parameters = DscConfigurationUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
