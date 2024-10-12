from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.event_hub_connection import EventHubConnection
from openapi_server.models.event_hub_connection_list_result import EventHubConnectionListResult
from openapi_server.models.event_hub_connection_update import EventHubConnectionUpdate
from openapi_server.models.event_hub_connection_validation import EventHubConnectionValidation
from openapi_server.models.event_hub_connection_validation_list_result import EventHubConnectionValidationListResult
from openapi_server import util


async def event_hub_connections_create_or_update(request: web.Request, resource_group_name, cluster_name, database_name, event_hub_connection_name, subscription_id, api_version, parameters) -> web.Response:
    """event_hub_connections_create_or_update

    Creates or updates a Event Hub connection.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param database_name: The name of the database in the Kusto cluster.
    :type database_name: str
    :param event_hub_connection_name: The name of the event hub connection.
    :type event_hub_connection_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param parameters: The Event Hub connection parameters supplied to the CreateOrUpdate operation.
    :type parameters: dict | bytes

    """
    parameters = EventHubConnection.from_dict(parameters)
    return web.Response(status=200)


async def event_hub_connections_delete(request: web.Request, resource_group_name, cluster_name, database_name, event_hub_connection_name, subscription_id, api_version) -> web.Response:
    """event_hub_connections_delete

    Deletes the Event Hub connection with the given name.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param database_name: The name of the database in the Kusto cluster.
    :type database_name: str
    :param event_hub_connection_name: The name of the event hub connection.
    :type event_hub_connection_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def event_hub_connections_eventhub_connection_validation(request: web.Request, resource_group_name, cluster_name, database_name, api_version, subscription_id, parameters) -> web.Response:
    """event_hub_connections_eventhub_connection_validation

    Checks that the Event Hub data connection parameters are valid.

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
    :param parameters: The Event Hub connection parameters supplied to the CreateOrUpdate operation.
    :type parameters: dict | bytes

    """
    parameters = EventHubConnectionValidation.from_dict(parameters)
    return web.Response(status=200)


async def event_hub_connections_get(request: web.Request, resource_group_name, cluster_name, database_name, event_hub_connection_name, subscription_id, api_version) -> web.Response:
    """event_hub_connections_get

    Returns an Event Hub connection.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param database_name: The name of the database in the Kusto cluster.
    :type database_name: str
    :param event_hub_connection_name: The name of the event hub connection.
    :type event_hub_connection_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def event_hub_connections_list_by_database(request: web.Request, resource_group_name, cluster_name, database_name, subscription_id, api_version) -> web.Response:
    """event_hub_connections_list_by_database

    Returns the list of Event Hub connections of the given Kusto database.

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


async def event_hub_connections_update(request: web.Request, resource_group_name, cluster_name, database_name, event_hub_connection_name, subscription_id, api_version, parameters) -> web.Response:
    """event_hub_connections_update

    Updates a Event Hub connection.

    :param resource_group_name: The name of the resource group containing the Kusto cluster.
    :type resource_group_name: str
    :param cluster_name: The name of the Kusto cluster.
    :type cluster_name: str
    :param database_name: The name of the database in the Kusto cluster.
    :type database_name: str
    :param event_hub_connection_name: The name of the event hub connection.
    :type event_hub_connection_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param parameters: The Event Hub connection parameters supplied to the Update operation.
    :type parameters: dict | bytes

    """
    parameters = EventHubConnectionUpdate.from_dict(parameters)
    return web.Response(status=200)
