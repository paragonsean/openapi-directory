from typing import List, Dict
from aiohttp import web

from openapi_server.models.disaster_recovery_configuration import DisasterRecoveryConfiguration
from openapi_server.models.disaster_recovery_configuration_list_result import DisasterRecoveryConfigurationListResult
from openapi_server import util


async def disaster_recovery_configurations_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, server_name, disaster_recovery_configuration_name) -> web.Response:
    """disaster_recovery_configurations_create_or_update

    Creates or updates a disaster recovery configuration.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param disaster_recovery_configuration_name: The name of the disaster recovery configuration to be created/updated.
    :type disaster_recovery_configuration_name: str

    """
    return web.Response(status=200)


async def disaster_recovery_configurations_delete(request: web.Request, api_version, subscription_id, resource_group_name, server_name, disaster_recovery_configuration_name) -> web.Response:
    """disaster_recovery_configurations_delete

    Deletes a disaster recovery configuration.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param disaster_recovery_configuration_name: The name of the disaster recovery configuration to be deleted.
    :type disaster_recovery_configuration_name: str

    """
    return web.Response(status=200)


async def disaster_recovery_configurations_failover(request: web.Request, api_version, subscription_id, resource_group_name, server_name, disaster_recovery_configuration_name) -> web.Response:
    """disaster_recovery_configurations_failover

    Fails over from the current primary server to this server.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param disaster_recovery_configuration_name: The name of the disaster recovery configuration to failover.
    :type disaster_recovery_configuration_name: str

    """
    return web.Response(status=200)


async def disaster_recovery_configurations_failover_allow_data_loss(request: web.Request, api_version, subscription_id, resource_group_name, server_name, disaster_recovery_configuration_name) -> web.Response:
    """disaster_recovery_configurations_failover_allow_data_loss

    Fails over from the current primary server to this server. This operation might result in data loss.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param disaster_recovery_configuration_name: The name of the disaster recovery configuration to failover forcefully.
    :type disaster_recovery_configuration_name: str

    """
    return web.Response(status=200)


async def disaster_recovery_configurations_get(request: web.Request, api_version, subscription_id, resource_group_name, server_name, disaster_recovery_configuration_name) -> web.Response:
    """disaster_recovery_configurations_get

    Gets a disaster recovery configuration.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param disaster_recovery_configuration_name: The name of the disaster recovery configuration.
    :type disaster_recovery_configuration_name: str

    """
    return web.Response(status=200)


async def disaster_recovery_configurations_list(request: web.Request, api_version, subscription_id, resource_group_name, server_name) -> web.Response:
    """disaster_recovery_configurations_list

    Lists a server&#39;s disaster recovery configuration.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str

    """
    return web.Response(status=200)
