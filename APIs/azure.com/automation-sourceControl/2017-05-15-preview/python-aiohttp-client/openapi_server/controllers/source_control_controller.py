from typing import List, Dict
from aiohttp import web

from openapi_server.models.source_control import SourceControl
from openapi_server.models.source_control_create_or_update_parameters import SourceControlCreateOrUpdateParameters
from openapi_server.models.source_control_list_by_automation_account_default_response import SourceControlListByAutomationAccountDefaultResponse
from openapi_server.models.source_control_list_result import SourceControlListResult
from openapi_server.models.source_control_update_parameters import SourceControlUpdateParameters
from openapi_server import util


async def source_control_create_or_update(request: web.Request, resource_group_name, automation_account_name, source_control_name, subscription_id, api_version, parameters) -> web.Response:
    """source_control_create_or_update

    Create a source control.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param source_control_name: The source control name.
    :type source_control_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters supplied to the create or update source control operation.
    :type parameters: dict | bytes

    """
    parameters = SourceControlCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def source_control_delete(request: web.Request, resource_group_name, automation_account_name, source_control_name, subscription_id, api_version) -> web.Response:
    """source_control_delete

    Delete the source control.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param source_control_name: The name of source control.
    :type source_control_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def source_control_get(request: web.Request, resource_group_name, automation_account_name, source_control_name, subscription_id, api_version) -> web.Response:
    """source_control_get

    Retrieve the source control identified by source control name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param source_control_name: The name of source control.
    :type source_control_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def source_control_list_by_automation_account(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version, filter=None) -> web.Response:
    """source_control_list_by_automation_account

    Retrieve a list of source controls.

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


async def source_control_update(request: web.Request, resource_group_name, automation_account_name, source_control_name, subscription_id, api_version, parameters) -> web.Response:
    """source_control_update

    Update a source control.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param source_control_name: The source control name.
    :type source_control_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters supplied to the update source control operation.
    :type parameters: dict | bytes

    """
    parameters = SourceControlUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
