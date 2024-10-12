from typing import List, Dict
from aiohttp import web

from openapi_server.models.connection_type import ConnectionType
from openapi_server.models.connection_type_create_or_update_parameters import ConnectionTypeCreateOrUpdateParameters
from openapi_server.models.connection_type_list_by_automation_account_default_response import ConnectionTypeListByAutomationAccountDefaultResponse
from openapi_server.models.connection_type_list_result import ConnectionTypeListResult
from openapi_server import util


async def connection_type_create_or_update(request: web.Request, resource_group_name, automation_account_name, connection_type_name, subscription_id, api_version, parameters) -> web.Response:
    """connection_type_create_or_update

    Create a connection type.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param connection_type_name: The parameters supplied to the create or update connection type operation.
    :type connection_type_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters supplied to the create or update connection type operation.
    :type parameters: dict | bytes

    """
    parameters = ConnectionTypeCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def connection_type_delete(request: web.Request, resource_group_name, automation_account_name, connection_type_name, subscription_id, api_version) -> web.Response:
    """connection_type_delete

    Delete the connection type.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param connection_type_name: The name of connection type.
    :type connection_type_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def connection_type_get(request: web.Request, resource_group_name, automation_account_name, connection_type_name, subscription_id, api_version) -> web.Response:
    """connection_type_get

    Retrieve the connection type identified by connection type name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param connection_type_name: The name of connection type.
    :type connection_type_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def connection_type_list_by_automation_account(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version) -> web.Response:
    """connection_type_list_by_automation_account

    Retrieve a list of connection types.

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
