from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_configuration import BatchConfiguration
from openapi_server.models.batch_configuration_collection import BatchConfigurationCollection
from openapi_server import util


async def integration_account_batch_configurations_create_or_update(request: web.Request, subscription_id, resource_group_name, integration_account_name, batch_configuration_name, api_version, batch_configuration) -> web.Response:
    """integration_account_batch_configurations_create_or_update

    Create or update a batch configuration for an integration account.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param batch_configuration_name: The batch configuration name.
    :type batch_configuration_name: str
    :param api_version: The API version.
    :type api_version: str
    :param batch_configuration: The batch configuration.
    :type batch_configuration: dict | bytes

    """
    batch_configuration = BatchConfiguration.from_dict(batch_configuration)
    return web.Response(status=200)


async def integration_account_batch_configurations_delete(request: web.Request, subscription_id, resource_group_name, integration_account_name, batch_configuration_name, api_version) -> web.Response:
    """integration_account_batch_configurations_delete

    Delete a batch configuration for an integration account.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param batch_configuration_name: The batch configuration name.
    :type batch_configuration_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_account_batch_configurations_get(request: web.Request, subscription_id, resource_group_name, integration_account_name, batch_configuration_name, api_version) -> web.Response:
    """integration_account_batch_configurations_get

    Get a batch configuration for an integration account.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param batch_configuration_name: The batch configuration name.
    :type batch_configuration_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_account_batch_configurations_list(request: web.Request, subscription_id, resource_group_name, integration_account_name, api_version) -> web.Response:
    """integration_account_batch_configurations_list

    List the batch configurations for an integration account.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)
