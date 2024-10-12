from typing import List, Dict
from aiohttp import web

from openapi_server.models.database_automatic_tuning import DatabaseAutomaticTuning
from openapi_server import util


async def database_automatic_tuning_get(request: web.Request, resource_group_name, server_name, database_name, subscription_id, api_version) -> web.Response:
    """database_automatic_tuning_get

    Gets a database&#39;s automatic tuning.

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

    """
    return web.Response(status=200)


async def database_automatic_tuning_update(request: web.Request, resource_group_name, server_name, database_name, subscription_id, api_version, parameters) -> web.Response:
    """database_automatic_tuning_update

    Update automatic tuning properties for target database.

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
    :param parameters: The requested automatic tuning resource state.
    :type parameters: dict | bytes

    """
    parameters = DatabaseAutomaticTuning.from_dict(parameters)
    return web.Response(status=200)
