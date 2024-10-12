from typing import List, Dict
from aiohttp import web

from openapi_server.models.recommended_action import RecommendedAction
from openapi_server import util


async def database_recommended_actions_get(request: web.Request, resource_group_name, server_name, database_name, advisor_name, recommended_action_name, subscription_id, api_version) -> web.Response:
    """database_recommended_actions_get

    Gets a database recommended action.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param advisor_name: The name of the Database Advisor.
    :type advisor_name: str
    :param recommended_action_name: The name of Database Recommended Action.
    :type recommended_action_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def database_recommended_actions_list_by_database_advisor(request: web.Request, resource_group_name, server_name, database_name, advisor_name, subscription_id, api_version) -> web.Response:
    """database_recommended_actions_list_by_database_advisor

    Gets list of Database Recommended Actions.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param advisor_name: The name of the Database Advisor.
    :type advisor_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def database_recommended_actions_update(request: web.Request, resource_group_name, server_name, database_name, advisor_name, recommended_action_name, subscription_id, api_version, parameters) -> web.Response:
    """database_recommended_actions_update

    Updates a database recommended action.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param advisor_name: The name of the Database Advisor.
    :type advisor_name: str
    :param recommended_action_name: The name of Database Recommended Action.
    :type recommended_action_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested recommended action resource state.
    :type parameters: dict | bytes

    """
    parameters = RecommendedAction.from_dict(parameters)
    return web.Response(status=200)
