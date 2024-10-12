from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def create_recommended_action_session(request: web.Request, api_version, subscription_id, resource_group_name, server_name, advisor_name, database_name) -> web.Response:
    """create_recommended_action_session

    Create recommendation action session for the advisor.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param advisor_name: The advisor name for recommendation action.
    :type advisor_name: str
    :param database_name: The name of the database.
    :type database_name: str

    """
    return web.Response(status=200)
