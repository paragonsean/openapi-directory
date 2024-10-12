from typing import List, Dict
from aiohttp import web

from openapi_server.models.database_schema import DatabaseSchema
from openapi_server.models.database_schema_list_result import DatabaseSchemaListResult
from openapi_server import util


async def database_schemas_get(request: web.Request, resource_group_name, server_name, database_name, schema_name, subscription_id, api_version) -> web.Response:
    """database_schemas_get

    Get database schema

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param schema_name: The name of the schema.
    :type schema_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def database_schemas_list_by_database(request: web.Request, resource_group_name, server_name, database_name, subscription_id, api_version, filter=None) -> web.Response:
    """database_schemas_list_by_database

    List database schemas

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param filter: An OData filter expression that filters elements in the collection.
    :type filter: str

    """
    return web.Response(status=200)
