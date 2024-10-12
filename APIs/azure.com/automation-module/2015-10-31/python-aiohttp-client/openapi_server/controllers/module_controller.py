from typing import List, Dict
from aiohttp import web

from openapi_server.models.module import Module
from openapi_server.models.module_create_or_update_parameters import ModuleCreateOrUpdateParameters
from openapi_server.models.module_list_by_automation_account_default_response import ModuleListByAutomationAccountDefaultResponse
from openapi_server.models.module_list_result import ModuleListResult
from openapi_server.models.module_update_parameters import ModuleUpdateParameters
from openapi_server import util


async def module_create_or_update(request: web.Request, resource_group_name, automation_account_name, module_name, subscription_id, api_version, parameters) -> web.Response:
    """module_create_or_update

    Create or Update the module identified by module name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param module_name: The name of module.
    :type module_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The create or update parameters for module.
    :type parameters: dict | bytes

    """
    parameters = ModuleCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def module_delete(request: web.Request, resource_group_name, automation_account_name, module_name, subscription_id, api_version) -> web.Response:
    """module_delete

    Delete the module by name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param module_name: The module name.
    :type module_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def module_get(request: web.Request, resource_group_name, automation_account_name, module_name, subscription_id, api_version) -> web.Response:
    """module_get

    Retrieve the module identified by module name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param module_name: The module name.
    :type module_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def module_list_by_automation_account(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version) -> web.Response:
    """module_list_by_automation_account

    Retrieve a list of modules.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def module_update(request: web.Request, resource_group_name, automation_account_name, module_name, subscription_id, api_version, parameters) -> web.Response:
    """module_update

    Update the module identified by module name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param module_name: The name of module.
    :type module_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The update parameters for module.
    :type parameters: dict | bytes

    """
    parameters = ModuleUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
