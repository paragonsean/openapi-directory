from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.migration_config_list_result import MigrationConfigListResult
from openapi_server.models.migration_config_properties import MigrationConfigProperties
from openapi_server import util


async def migration_configs_complete_migration(request: web.Request, resource_group_name, namespace_name, config_name, api_version, subscription_id) -> web.Response:
    """migration_configs_complete_migration

    This operation Completes Migration of entities by pointing the connection strings to Premium namespace and any entities created after the operation will be under Premium Namespace. CompleteMigration operation will fail when entity migration is in-progress.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param config_name: The configuration name. Should always be \&quot;$default\&quot;.
    :type config_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def migration_configs_create_and_start_migration(request: web.Request, resource_group_name, namespace_name, config_name, api_version, subscription_id, parameters) -> web.Response:
    """migration_configs_create_and_start_migration

    Creates Migration configuration and starts migration of entities from Standard to Premium namespace

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param config_name: The configuration name. Should always be \&quot;$default\&quot;.
    :type config_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters required to create Migration Configuration
    :type parameters: dict | bytes

    """
    parameters = MigrationConfigProperties.from_dict(parameters)
    return web.Response(status=200)


async def migration_configs_delete(request: web.Request, resource_group_name, namespace_name, config_name, api_version, subscription_id) -> web.Response:
    """migration_configs_delete

    Deletes a MigrationConfiguration

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param config_name: The configuration name. Should always be \&quot;$default\&quot;.
    :type config_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def migration_configs_get(request: web.Request, resource_group_name, namespace_name, config_name, api_version, subscription_id) -> web.Response:
    """migration_configs_get

    Retrieves Migration Config

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param config_name: The configuration name. Should always be \&quot;$default\&quot;.
    :type config_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def migration_configs_list(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id) -> web.Response:
    """migration_configs_list

    Gets all migrationConfigurations

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def migration_configs_revert(request: web.Request, resource_group_name, namespace_name, config_name, api_version, subscription_id) -> web.Response:
    """migration_configs_revert

    This operation reverts Migration

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param config_name: The configuration name. Should always be \&quot;$default\&quot;.
    :type config_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
