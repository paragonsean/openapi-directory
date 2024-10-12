from typing import List, Dict
from aiohttp import web

from openapi_server.models.build_beta_notification_create_request import BuildBetaNotificationCreateRequest
from openapi_server.models.build_beta_notification_response import BuildBetaNotificationResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def build_beta_notifications_create_instance(request: web.Request, body) -> web.Response:
    """build_beta_notifications_create_instance

    

    :param body: BuildBetaNotification representation
    :type body: dict | bytes

    """
    body = BuildBetaNotificationCreateRequest.from_dict(body)
    return web.Response(status=200)
