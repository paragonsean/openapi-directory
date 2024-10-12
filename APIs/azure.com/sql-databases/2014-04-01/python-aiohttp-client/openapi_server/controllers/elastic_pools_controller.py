from typing import List, Dict
from aiohttp import web

from openapi_server.models.database import Database
from openapi_server import util


async def databases_get_by_elastic_pool(request: web.Request, api_version, subscription_id, resource_group_name, server_name, elastic_pool_name, database_name) -> web.Response:
    """databases_get_by_elastic_pool

    Gets a database inside of an elastic pool.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param elastic_pool_name: The name of the elastic pool to be retrieved.
    :type elastic_pool_name: str
    :param database_name: The name of the database to be retrieved.
    :type database_name: str

    """
    return web.Response(status=200)
