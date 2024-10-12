from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_models_notification import APIModelsNotification
from openapi_server import util


async def notifications_post_mail(request: web.Request, body) -> web.Response:
    """Sends an email message.

    No Documentation Found.

    :param body: The Notification Object.
    :type body: dict | bytes

    """
    body = APIModelsNotification.from_dict(body)
    return web.Response(status=200)
