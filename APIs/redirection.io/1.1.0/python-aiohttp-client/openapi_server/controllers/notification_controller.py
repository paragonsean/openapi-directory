from typing import List, Dict
from aiohttp import web

from openapi_server.models.notification_read import NotificationRead
from openapi_server import util


async def get_notification_collection(request: web.Request, page=None) -> web.Response:
    """Retrieves the collection of Notification resources.

    

    :param page: The collection page number
    :type page: int

    """
    return web.Response(status=200)


async def get_notification_item(request: web.Request, id) -> web.Response:
    """Retrieves a Notification resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
