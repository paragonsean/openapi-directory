from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_result import CheckNameResult
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.data_connection import DataConnection
from openapi_server.models.data_connection_check_name_request import DataConnectionCheckNameRequest
from openapi_server.models.data_connection_list_result import DataConnectionListResult
from openapi_server.models.data_connection_validation import DataConnectionValidation
from openapi_server.models.data_connection_validation_list_result import DataConnectionValidationListResult
from openapi_server import util


async def data_connections_check_name_availability(request: web.Request, resource_group_name, cluster_name, database_name, api_version, subscription_id, data_connection_name) -> web.Response:
    """data_connections_check_name_availability

    Checks that the data connection name is valid and is not already in use.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param database_name: The name of the database in the Kusto cluster.
    :type database_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param data_connection_name: The name of the data connection.
    :type data_connection_name: dict | bytes

    """
    data_connection_name = DataConnectionCheckNameRequest.from_dict(data_connection_name)
    return web.Response(status=200)


async def data_connections_create_or_update(request: web.Request, resource_group_name, cluster_name, database_name, data_connection_name, subscription_id, api_version, parameters) -> web.Response:
    """data_connections_create_or_update

    Creates or updates a data connection.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param database_name: The name of the database in the Kusto cluster.
    :type database_name: str
    :param data_connection_name: The name of the data connection.
    :type data_connection_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param parameters: The data connection parameters supplied to the CreateOrUpdate operation.
    :type parameters: dict | bytes

    """
    parameters = DataConnection.from_dict(parameters)
    return web.Response(status=200)


async def data_connections_data_connection_validation(request: web.Request, resource_group_name, cluster_name, database_name, api_version, subscription_id, parameters) -> web.Response:
    """data_connections_data_connection_validation

    Checks that the data connection parameters are valid.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param database_name: The name of the database in the Kusto cluster.
    :type database_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The data connection parameters supplied to the CreateOrUpdate operation.
    :type parameters: dict | bytes

    """
    parameters = DataConnectionValidation.from_dict(parameters)
    return web.Response(status=200)


async def data_connections_delete(request: web.Request, resource_group_name, cluster_name, database_name, data_connection_name, subscription_id, api_version) -> web.Response:
    """data_connections_delete

    Deletes the data connection with the given name.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param database_name: The name of the database in the Kusto cluster.
    :type database_name: str
    :param data_connection_name: The name of the data connection.
    :type data_connection_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def data_connections_get(request: web.Request, resource_group_name, cluster_name, database_name, data_connection_name, subscription_id, api_version) -> web.Response:
    """data_connections_get

    Returns a data connection.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param database_name: The name of the database in the Kusto cluster.
    :type database_name: str
    :param data_connection_name: The name of the data connection.
    :type data_connection_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def data_connections_list_by_database(request: web.Request, resource_group_name, cluster_name, database_name, subscription_id, api_version) -> web.Response:
    """data_connections_list_by_database

    Returns the list of data connections of the given Kusto database.

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


async def data_connections_update(request: web.Request, resource_group_name, cluster_name, database_name, data_connection_name, subscription_id, api_version, parameters) -> web.Response:
    """data_connections_update

    Updates a data connection.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param database_name: The name of the database in the Kusto cluster.
    :type database_name: str
    :param data_connection_name: The name of the data connection.
    :type data_connection_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param parameters: The data connection parameters supplied to the Update operation.
    :type parameters: dict | bytes

    """
    parameters = DataConnection.from_dict(parameters)
    return web.Response(status=200)
