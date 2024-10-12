from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_pkg_notification import AppPkgNotification
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def app_pkg_notification_post(request: web.Request, body) -> web.Response:
    """Registers a notification endpoint to notify application package operations

    Registers a notification endpoint to notify application package operations

    :param body: Notification endpoint to be created
    :type body: dict | bytes

    """
    body = AppPkgNotification.from_dict(body)
    return web.Response(status=200)
