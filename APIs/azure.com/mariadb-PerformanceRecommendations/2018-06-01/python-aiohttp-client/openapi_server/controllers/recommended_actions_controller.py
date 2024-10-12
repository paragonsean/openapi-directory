from typing import List, Dict
from aiohttp import web

from openapi_server.models.recommendation_action import RecommendationAction
from openapi_server.models.recommendation_actions_result_list import RecommendationActionsResultList
from openapi_server import util


async def recommended_actions_get(request: web.Request, api_version, subscription_id, resource_group_name, server_name, advisor_name, recommended_action_name) -> web.Response:
    """recommended_actions_get

    Retrieve recommended actions from the advisor.

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
    :param recommended_action_name: The recommended action name.
    :type recommended_action_name: str

    """
    return web.Response(status=200)


async def recommended_actions_list_by_server(request: web.Request, api_version, subscription_id, resource_group_name, server_name, advisor_name, session_id=None) -> web.Response:
    """recommended_actions_list_by_server

    Retrieve recommended actions from the advisor.

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
    :param session_id: The recommendation action session identifier.
    :type session_id: str

    """
    return web.Response(status=200)
