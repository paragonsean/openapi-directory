from typing import List, Dict
from aiohttp import web

from openapi_server.models.variable import Variable
from openapi_server.models.variable_create_or_update_parameters import VariableCreateOrUpdateParameters
from openapi_server.models.variable_list_by_automation_account_default_response import VariableListByAutomationAccountDefaultResponse
from openapi_server.models.variable_list_result import VariableListResult
from openapi_server.models.variable_update_parameters import VariableUpdateParameters
from openapi_server import util


async def variable_create_or_update(request: web.Request, resource_group_name, automation_account_name, variable_name, subscription_id, api_version, parameters) -> web.Response:
    """variable_create_or_update

    Create a variable.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param variable_name: The variable name.
    :type variable_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters supplied to the create or update variable operation.
    :type parameters: dict | bytes

    """
    parameters = VariableCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def variable_delete(request: web.Request, resource_group_name, automation_account_name, variable_name, subscription_id, api_version) -> web.Response:
    """variable_delete

    Delete the variable.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param variable_name: The name of variable.
    :type variable_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def variable_get(request: web.Request, resource_group_name, automation_account_name, variable_name, subscription_id, api_version) -> web.Response:
    """variable_get

    Retrieve the variable identified by variable name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param variable_name: The name of variable.
    :type variable_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def variable_list_by_automation_account(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version) -> web.Response:
    """variable_list_by_automation_account

    Retrieve a list of variables.

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


async def variable_update(request: web.Request, resource_group_name, automation_account_name, variable_name, subscription_id, api_version, parameters) -> web.Response:
    """variable_update

    Update a variable.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param variable_name: The variable name.
    :type variable_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters supplied to the update variable operation.
    :type parameters: dict | bytes

    """
    parameters = VariableUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
