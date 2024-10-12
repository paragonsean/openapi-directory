from typing import List, Dict
from aiohttp import web

from openapi_server.models.software_update_configuration import SoftwareUpdateConfiguration
from openapi_server.models.software_update_configuration_list_result import SoftwareUpdateConfigurationListResult
from openapi_server.models.software_update_configurations_list_default_response import SoftwareUpdateConfigurationsListDefaultResponse
from openapi_server import util


async def software_update_configurations_create(request: web.Request, subscription_id, resource_group_name, automation_account_name, software_update_configuration_name, api_version, parameters, client_request_id=None) -> web.Response:
    """software_update_configurations_create

    Create a new software update configuration with the name given in the URI.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param software_update_configuration_name: The name of the software update configuration to be created.
    :type software_update_configuration_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: Request body.
    :type parameters: dict | bytes
    :param client_request_id: Identifies this specific client request.
    :type client_request_id: str

    """
    parameters = SoftwareUpdateConfiguration.from_dict(parameters)
    return web.Response(status=200)


async def software_update_configurations_delete(request: web.Request, subscription_id, resource_group_name, automation_account_name, software_update_configuration_name, api_version, client_request_id=None) -> web.Response:
    """software_update_configurations_delete

    delete a specific software update configuration.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param software_update_configuration_name: The name of the software update configuration to be created.
    :type software_update_configuration_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param client_request_id: Identifies this specific client request.
    :type client_request_id: str

    """
    return web.Response(status=200)


async def software_update_configurations_get_by_name(request: web.Request, subscription_id, resource_group_name, automation_account_name, software_update_configuration_name, api_version, client_request_id=None) -> web.Response:
    """software_update_configurations_get_by_name

    Get a single software update configuration by name.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param software_update_configuration_name: The name of the software update configuration to be created.
    :type software_update_configuration_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param client_request_id: Identifies this specific client request.
    :type client_request_id: str

    """
    return web.Response(status=200)


async def software_update_configurations_list(request: web.Request, subscription_id, resource_group_name, automation_account_name, api_version, client_request_id=None, filter=None) -> web.Response:
    """software_update_configurations_list

    Get all software update configurations for the account.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param client_request_id: Identifies this specific client request.
    :type client_request_id: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)
