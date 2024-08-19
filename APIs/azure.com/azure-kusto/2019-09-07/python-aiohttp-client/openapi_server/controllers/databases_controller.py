from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_request import CheckNameRequest
from openapi_server.models.check_name_result import CheckNameResult
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.database import Database
from openapi_server.models.database_list_result import DatabaseListResult
from openapi_server.models.database_principal_list_request import DatabasePrincipalListRequest
from openapi_server.models.database_principal_list_result import DatabasePrincipalListResult
from openapi_server import util


async def databases_add_principals(request: web.Request, resource_group_name, cluster_name, database_name, subscription_id, api_version, database_principals_to_add) -> web.Response:
    """databases_add_principals

    Add Database principals permissions.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param database_name: The name of the database in the Kusto cluster.
    :type database_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param database_principals_to_add: List of database principals to add.
    :type database_principals_to_add: dict | bytes

    """
    database_principals_to_add = DatabasePrincipalListRequest.from_dict(database_principals_to_add)
    return web.Response(status=200)


async def databases_check_name_availability(request: web.Request, resource_group_name, cluster_name, api_version, subscription_id, resource_name) -> web.Response:
    """databases_check_name_availability

    Checks that the database name is valid and is not already in use.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_name: The name of the resource.
    :type resource_name: dict | bytes

    """
    resource_name = CheckNameRequest.from_dict(resource_name)
    return web.Response(status=200)


async def databases_create_or_update(request: web.Request, resource_group_name, cluster_name, database_name, subscription_id, api_version, parameters) -> web.Response:
    """databases_create_or_update

    Creates or updates a database.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param database_name: The name of the database in the Kusto cluster.
    :type database_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param parameters: The database parameters supplied to the CreateOrUpdate operation.
    :type parameters: dict | bytes

    """
    parameters = Database.from_dict(parameters)
    return web.Response(status=200)


async def databases_delete(request: web.Request, resource_group_name, cluster_name, database_name, subscription_id, api_version) -> web.Response:
    """databases_delete

    Deletes the database with the given name.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param database_name: The name of the database in the Kusto cluster.
    :type database_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def databases_get(request: web.Request, resource_group_name, cluster_name, database_name, subscription_id, api_version) -> web.Response:
    """databases_get

    Returns a database.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param database_name: The name of the database in the Kusto cluster.
    :type database_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def databases_list_by_cluster(request: web.Request, resource_group_name, cluster_name, subscription_id, api_version) -> web.Response:
    """databases_list_by_cluster

    Returns the list of databases of the given Kusto cluster.

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


async def databases_list_principals(request: web.Request, resource_group_name, cluster_name, database_name, subscription_id, api_version) -> web.Response:
    """databases_list_principals

    Returns a list of database principals of the given Kusto cluster and database.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param database_name: The name of the database in the Kusto cluster.
    :type database_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def databases_remove_principals(request: web.Request, resource_group_name, cluster_name, database_name, subscription_id, api_version, database_principals_to_remove) -> web.Response:
    """databases_remove_principals

    Remove Database principals permissions.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param database_name: The name of the database in the Kusto cluster.
    :type database_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param database_principals_to_remove: List of database principals to remove.
    :type database_principals_to_remove: dict | bytes

    """
    database_principals_to_remove = DatabasePrincipalListRequest.from_dict(database_principals_to_remove)
    return web.Response(status=200)


async def databases_update(request: web.Request, resource_group_name, cluster_name, database_name, subscription_id, api_version, parameters) -> web.Response:
    """databases_update

    Updates a database.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param database_name: The name of the database in the Kusto cluster.
    :type database_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param parameters: The database parameters supplied to the Update operation.
    :type parameters: dict | bytes

    """
    parameters = Database.from_dict(parameters)
    return web.Response(status=200)
