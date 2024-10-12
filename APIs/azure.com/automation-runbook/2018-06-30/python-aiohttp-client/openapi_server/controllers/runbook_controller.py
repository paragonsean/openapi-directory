from typing import List, Dict
from aiohttp import web

from openapi_server.models.runbook import Runbook
from openapi_server.models.runbook_create_or_update_parameters import RunbookCreateOrUpdateParameters
from openapi_server.models.runbook_list_by_automation_account_default_response import RunbookListByAutomationAccountDefaultResponse
from openapi_server.models.runbook_list_result import RunbookListResult
from openapi_server.models.runbook_update_parameters import RunbookUpdateParameters
from openapi_server import util


async def runbook_create_or_update(request: web.Request, subscription_id, resource_group_name, automation_account_name, runbook_name, api_version, parameters) -> web.Response:
    """runbook_create_or_update

    Create the runbook identified by runbook name.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param runbook_name: The runbook name.
    :type runbook_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The create or update parameters for runbook. Provide either content link for a published runbook or draft, not both.
    :type parameters: dict | bytes

    """
    parameters = RunbookCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def runbook_delete(request: web.Request, subscription_id, resource_group_name, automation_account_name, runbook_name, api_version) -> web.Response:
    """runbook_delete

    Delete the runbook by name.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param runbook_name: The runbook name.
    :type runbook_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def runbook_get(request: web.Request, subscription_id, resource_group_name, automation_account_name, runbook_name, api_version) -> web.Response:
    """runbook_get

    Retrieve the runbook identified by runbook name.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param runbook_name: The runbook name.
    :type runbook_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def runbook_get_content(request: web.Request, subscription_id, resource_group_name, automation_account_name, runbook_name, api_version) -> web.Response:
    """runbook_get_content

    Retrieve the content of runbook identified by runbook name.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param runbook_name: The runbook name.
    :type runbook_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def runbook_list_by_automation_account(request: web.Request, subscription_id, resource_group_name, automation_account_name, api_version) -> web.Response:
    """runbook_list_by_automation_account

    Retrieve a list of runbooks.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def runbook_publish(request: web.Request, subscription_id, resource_group_name, automation_account_name, runbook_name, api_version) -> web.Response:
    """runbook_publish

    Publish runbook draft.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param runbook_name: The parameters supplied to the publish runbook operation.
    :type runbook_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def runbook_update(request: web.Request, subscription_id, resource_group_name, automation_account_name, runbook_name, api_version, parameters) -> web.Response:
    """runbook_update

    Update the runbook identified by runbook name.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param runbook_name: The runbook name.
    :type runbook_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The update parameters for runbook.
    :type parameters: dict | bytes

    """
    parameters = RunbookUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
