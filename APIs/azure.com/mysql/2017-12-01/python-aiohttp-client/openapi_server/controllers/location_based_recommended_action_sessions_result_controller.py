from typing import List, Dict
from aiohttp import web

from openapi_server.models.recommendation_actions_result_list import RecommendationActionsResultList
from openapi_server import util


async def location_based_recommended_action_sessions_result_list(request: web.Request, api_version, subscription_id, location_name, operation_id) -> web.Response:
    """location_based_recommended_action_sessions_result_list

    Recommendation action session operation result.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param location_name: The name of the location.
    :type location_name: str
    :param operation_id: The operation identifier.
    :type operation_id: str

    """
    return web.Response(status=200)
