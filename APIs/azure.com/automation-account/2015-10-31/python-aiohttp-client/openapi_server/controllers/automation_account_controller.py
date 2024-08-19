from typing import List, Dict
from aiohttp import web

from openapi_server.models.automation_account import AutomationAccount
from openapi_server.models.automation_account_create_or_update_parameters import AutomationAccountCreateOrUpdateParameters
from openapi_server.models.automation_account_list_result import AutomationAccountListResult
from openapi_server.models.automation_account_update_parameters import AutomationAccountUpdateParameters
from openapi_server.models.operations_list_default_response import OperationsListDefaultResponse
from openapi_server import util


async def automation_account_create_or_update(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version, parameters) -> web.Response:
    """automation_account_create_or_update

    Create or update automation account.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to the create or update automation account.
    :type parameters: dict | bytes

    """
    parameters = AutomationAccountCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def automation_account_delete(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version) -> web.Response:
    """automation_account_delete

    Delete an automation account.

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


async def automation_account_get(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version) -> web.Response:
    """automation_account_get

    Get information about an Automation Account.

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


async def automation_account_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """Lists the Automation Accounts within an Azure subscription.

    Retrieve a list of accounts within a given subscription.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def automation_account_list_by_resource_group(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """automation_account_list_by_resource_group

    Retrieve a list of accounts within a given resource group.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def automation_account_update(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version, parameters) -> web.Response:
    """automation_account_update

    Update an automation account.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to the update automation account.
    :type parameters: dict | bytes

    """
    parameters = AutomationAccountUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
