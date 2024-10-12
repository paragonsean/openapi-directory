from typing import List, Dict
from aiohttp import web

from openapi_server.models.notification_preview import NotificationPreview
from openapi_server import util


async def notifications_contributions_id_preview_get(request: web.Request, id, message) -> web.Response:
    """notifications_contributions_id_preview_get

    

    :param id: Id of the contribution to preview a notification for
    :type id: str
    :param message: Type of message to preview.
    :type message: str

    """
    return web.Response(status=200)
