from typing import List, Dict
from aiohttp import web

from openapi_server.models.database_table import DatabaseTable
from openapi_server.models.database_table_list_result import DatabaseTableListResult
from openapi_server import util


async def database_tables_get(request: web.Request, resource_group_name, server_name, database_name, schema_name, table_name, subscription_id, api_version) -> web.Response:
    """database_tables_get

    Get database table

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param schema_name: The name of the schema.
    :type schema_name: str
    :param table_name: The name of the table.
    :type table_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def database_tables_list_by_schema(request: web.Request, resource_group_name, server_name, database_name, schema_name, subscription_id, api_version, filter=None) -> web.Response:
    """database_tables_list_by_schema

    List database tables

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
    :param filter: An OData filter expression that filters elements in the collection.
    :type filter: str

    """
    return web.Response(status=200)
