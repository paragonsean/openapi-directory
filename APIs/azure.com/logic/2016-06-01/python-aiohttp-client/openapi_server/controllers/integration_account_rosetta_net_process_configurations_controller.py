from typing import List, Dict
from aiohttp import web

from openapi_server.models.integration_account_rosetta_net_process_configuration import IntegrationAccountRosettaNetProcessConfiguration
from openapi_server.models.integration_account_rosetta_net_process_configuration_list_result import IntegrationAccountRosettaNetProcessConfigurationListResult
from openapi_server import util


async def rosetta_net_process_configurations_create_or_update(request: web.Request, subscription_id, resource_group_name, integration_account_name, rosetta_net_process_configuration_name, api_version, rosetta_net_process_configuration) -> web.Response:
    """rosetta_net_process_configurations_create_or_update

    Creates or updates an integration account RosettaNetProcessConfiguration.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param rosetta_net_process_configuration_name: The integration account RosettaNet ProcessConfiguration name.
    :type rosetta_net_process_configuration_name: str
    :param api_version: The API version.
    :type api_version: str
    :param rosetta_net_process_configuration: The integration account RosettaNet ProcessConfiguration.
    :type rosetta_net_process_configuration: dict | bytes

    """
    rosetta_net_process_configuration = IntegrationAccountRosettaNetProcessConfiguration.from_dict(rosetta_net_process_configuration)
    return web.Response(status=200)


async def rosetta_net_process_configurations_delete(request: web.Request, subscription_id, resource_group_name, integration_account_name, rosetta_net_process_configuration_name, api_version) -> web.Response:
    """rosetta_net_process_configurations_delete

    Deletes an integration account RosettaNet ProcessConfiguration.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param rosetta_net_process_configuration_name: The integration account RosettaNetProcessConfiguration name.
    :type rosetta_net_process_configuration_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def rosetta_net_process_configurations_get(request: web.Request, subscription_id, resource_group_name, integration_account_name, rosetta_net_process_configuration_name, api_version) -> web.Response:
    """rosetta_net_process_configurations_get

    Gets an integration account RosettaNetProcessConfiguration.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param rosetta_net_process_configuration_name: The integration account RosettaNetProcessConfiguration name.
    :type rosetta_net_process_configuration_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def rosetta_net_process_configurations_list_by_integration_accounts(request: web.Request, subscription_id, resource_group_name, integration_account_name, api_version, top=None, filter=None) -> web.Response:
    """rosetta_net_process_configurations_list_by_integration_accounts

    Gets a list of integration account RosettaNet process configurations.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param api_version: The API version.
    :type api_version: str
    :param top: The number of items to be included in the result.
    :type top: int
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)
