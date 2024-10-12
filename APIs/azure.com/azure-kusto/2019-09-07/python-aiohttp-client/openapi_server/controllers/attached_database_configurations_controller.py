from typing import List, Dict
from aiohttp import web

from openapi_server.models.attached_database_configuration import AttachedDatabaseConfiguration
from openapi_server.models.attached_database_configuration_list_result import AttachedDatabaseConfigurationListResult
from openapi_server.models.cloud_error import CloudError
from openapi_server import util


async def attached_database_configurations_create_or_update(request: web.Request, resource_group_name, cluster_name, attached_database_configuration_name, subscription_id, api_version, parameters) -> web.Response:
    """attached_database_configurations_create_or_update

    Creates or updates an attached database configuration.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param attached_database_configuration_name: The name of the attached database configuration.
    :type attached_database_configuration_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param parameters: The database parameters supplied to the CreateOrUpdate operation.
    :type parameters: dict | bytes

    """
    parameters = AttachedDatabaseConfiguration.from_dict(parameters)
    return web.Response(status=200)


async def attached_database_configurations_delete(request: web.Request, resource_group_name, cluster_name, attached_database_configuration_name, subscription_id, api_version) -> web.Response:
    """attached_database_configurations_delete

    Deletes the attached database configuration with the given name.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param attached_database_configuration_name: The name of the attached database configuration.
    :type attached_database_configuration_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def attached_database_configurations_get(request: web.Request, resource_group_name, cluster_name, attached_database_configuration_name, subscription_id, api_version) -> web.Response:
    """attached_database_configurations_get

    Returns an attached database configuration.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param attached_database_configuration_name: The name of the attached database configuration.
    :type attached_database_configuration_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def attached_database_configurations_list_by_cluster(request: web.Request, resource_group_name, cluster_name, subscription_id, api_version) -> web.Response:
    """attached_database_configurations_list_by_cluster

    Returns the list of attached database configurations of the given Kusto cluster.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)
