from typing import List, Dict
from aiohttp import web

from openapi_server.models.resource_move_definition import ResourceMoveDefinition
from openapi_server import util


async def databases_rename(request: web.Request, resource_group_name, server_name, database_name, subscription_id, api_version, parameters) -> web.Response:
    """databases_rename

    Renames a database.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database to rename.
    :type database_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The resource move definition for renaming this database.
    :type parameters: dict | bytes

    """
    parameters = ResourceMoveDefinition.from_dict(parameters)
    return web.Response(status=200)
