from typing import List, Dict
from aiohttp import web

from openapi_server.models.name_id_pair import NameIdPair
from openapi_server.models.notification_level import NotificationLevel
from openapi_server.models.notification_result_dto import NotificationResultDto
from openapi_server.models.notification_type_info import NotificationTypeInfo
from openapi_server.models.notifications_summary_dto import NotificationsSummaryDto
from openapi_server import util


async def create_admin_notification(request: web.Request, url=None, level=None, name=None, description=None) -> web.Response:
    """Sends a notification to all admins.

    

    :param url: The URL of the notification.
    :type url: str
    :param level: The level of the notification.
    :type level: dict | bytes
    :param name: The name of the notification.
    :type name: str
    :param description: The description of the notification.
    :type description: str

    """
    level = .from_dict(level)
    return web.Response(status=200)


async def get_notification_services(request: web.Request, ) -> web.Response:
    """Gets notification services.

    


    """
    return web.Response(status=200)


async def get_notification_types(request: web.Request, ) -> web.Response:
    """Gets notification types.

    


    """
    return web.Response(status=200)


async def get_notifications(request: web.Request, user_id) -> web.Response:
    """Gets a user&#39;s notifications.

    

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def get_notifications_summary(request: web.Request, user_id) -> web.Response:
    """Gets a user&#39;s notification summary.

    

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def set_read(request: web.Request, user_id) -> web.Response:
    """Sets notifications as read.

    

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def set_unread(request: web.Request, user_id) -> web.Response:
    """Sets notifications as unread.

    

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)
