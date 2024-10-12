from typing import List, Dict
from aiohttp import web

from openapi_server.models.recommended_action_sessions_operation_status import RecommendedActionSessionsOperationStatus
from openapi_server import util


async def location_based_recommended_action_sessions_operation_status_get(request: web.Request, api_version, subscription_id, location_name, operation_id) -> web.Response:
    """location_based_recommended_action_sessions_operation_status_get

    Recommendation action session operation status.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param location_name: The name of the location.
    :type location_name: str
    :param operation_id: The operation identifier.
    :type operation_id: str

    """
    return web.Response(status=200)
