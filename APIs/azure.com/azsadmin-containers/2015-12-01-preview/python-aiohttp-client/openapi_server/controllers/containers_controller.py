from typing import List, Dict
from aiohttp import web

from openapi_server.models.container import Container
from openapi_server.models.containers_list_destination_shares200_response_inner import ContainersListDestinationShares200ResponseInner
from openapi_server.models.migration_parameters import MigrationParameters
from openapi_server.models.migration_result import MigrationResult
from openapi_server import util


async def containers_cancel_migration(request: web.Request, subscription_id, resource_group_name, farm_id, operation_id, api_version) -> web.Response:
    """containers_cancel_migration

    Cancel a container migration job.

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param farm_id: Farm Id.
    :type farm_id: str
    :param operation_id: Operation Id.
    :type operation_id: str
    :param api_version: REST Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def containers_list(request: web.Request, subscription_id, resource_group_name, farm_id, share_name, api_version, intent, max_count=None, start_index=None) -> web.Response:
    """containers_list

    Returns the list of containers which can be migrated in the specified share.

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param farm_id: Farm Id.
    :type farm_id: str
    :param share_name: Share name.
    :type share_name: str
    :param api_version: REST Api Version.
    :type api_version: str
    :param intent: The container migration intent.
    :type intent: str
    :param max_count: The maximum number of containers.
    :type max_count: int
    :param start_index: The starting index the resource provider uses.
    :type start_index: int

    """
    return web.Response(status=200)


async def containers_list_destination_shares(request: web.Request, subscription_id, resource_group_name, farm_id, share_name, api_version) -> web.Response:
    """containers_list_destination_shares

    Returns a list of destination shares that the system considers as best candidates for migration.

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param farm_id: Farm Id.
    :type farm_id: str
    :param share_name: Share name.
    :type share_name: str
    :param api_version: REST Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def containers_migrate(request: web.Request, subscription_id, resource_group_name, farm_id, share_name, api_version, migration_parameters) -> web.Response:
    """containers_migrate

    Starts a container migration job to migrate containers to the specified destination share.

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param farm_id: Farm Id.
    :type farm_id: str
    :param share_name: Share name.
    :type share_name: str
    :param api_version: REST Api Version.
    :type api_version: str
    :param migration_parameters: The parameters of container migration job.
    :type migration_parameters: dict | bytes

    """
    migration_parameters = MigrationParameters.from_dict(migration_parameters)
    return web.Response(status=200)


async def containers_migration_status(request: web.Request, subscription_id, resource_group_name, farm_id, operation_id, api_version) -> web.Response:
    """containers_migration_status

    Returns the status of a container migration job.

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param farm_id: Farm Id.
    :type farm_id: str
    :param operation_id: Operation Id.
    :type operation_id: str
    :param api_version: REST Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
