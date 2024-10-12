from typing import List, Dict
from aiohttp import web

from openapi_server.models.database_usage_list_result import DatabaseUsageListResult
from openapi_server import util


async def database_usages_list_by_database(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name) -> web.Response:
    """database_usages_list_by_database

    Returns database usages.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str

    """
    return web.Response(status=200)
