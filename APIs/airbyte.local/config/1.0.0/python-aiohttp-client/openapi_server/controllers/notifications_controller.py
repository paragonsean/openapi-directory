from typing import List, Dict
from aiohttp import web

from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.notification import Notification
from openapi_server.models.notification_read import NotificationRead
from openapi_server import util


async def try_notification_config(request: web.Request, body) -> web.Response:
    """Try sending a notifications

    

    :param body: 
    :type body: dict | bytes

    """
    body = Notification.from_dict(body)
    return web.Response(status=200)
