from typing import List, Dict
from aiohttp import web

from openapi_server.models.connection import Connection
from openapi_server.models.connection_create_or_update_parameters import ConnectionCreateOrUpdateParameters
from openapi_server.models.connection_list_by_automation_account_default_response import ConnectionListByAutomationAccountDefaultResponse
from openapi_server.models.connection_list_result import ConnectionListResult
from openapi_server.models.connection_update_parameters import ConnectionUpdateParameters
from openapi_server import util


async def connection_create_or_update(request: web.Request, resource_group_name, automation_account_name, connection_name, subscription_id, api_version, parameters) -> web.Response:
    """connection_create_or_update

    Create or update a connection.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param connection_name: The parameters supplied to the create or update connection operation.
    :type connection_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters supplied to the create or update connection operation.
    :type parameters: dict | bytes

    """
    parameters = ConnectionCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def connection_delete(request: web.Request, resource_group_name, automation_account_name, connection_name, subscription_id, api_version) -> web.Response:
    """connection_delete

    Delete the connection.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param connection_name: The name of connection.
    :type connection_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def connection_get(request: web.Request, resource_group_name, automation_account_name, connection_name, subscription_id, api_version) -> web.Response:
    """connection_get

    Retrieve the connection identified by connection name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param connection_name: The name of connection.
    :type connection_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def connection_list_by_automation_account(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version) -> web.Response:
    """connection_list_by_automation_account

    Retrieve a list of connections.

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


async def connection_update(request: web.Request, resource_group_name, automation_account_name, connection_name, subscription_id, api_version, parameters) -> web.Response:
    """connection_update

    Update a connection.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param connection_name: The parameters supplied to the update a connection operation.
    :type connection_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters supplied to the update a connection operation.
    :type parameters: dict | bytes

    """
    parameters = ConnectionUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
