from typing import List, Dict
from aiohttp import web

from openapi_server.models.notification import Notification
from openapi_server.models.notification_type import NotificationType
from openapi_server import util


async def notifications_get(request: web.Request, all=None, user_id=None, device_id=None, group_id=None, refresh=None) -> web.Response:
    """Fetch a list of Notifications

    Without params, it returns a list of Notifications the user has access to

    :param all: Can only be used by admins or managers to fetch all entities
    :type all: bool
    :param user_id: Standard users can use this only with their own _userId_
    :type user_id: int
    :param device_id: Standard users can use this only with _deviceId_s, they have access to
    :type device_id: int
    :param group_id: Standard users can use this only with _groupId_s, they have access to
    :type group_id: int
    :param refresh: 
    :type refresh: bool

    """
    return web.Response(status=200)


async def notifications_id_delete(request: web.Request, id) -> web.Response:
    """Delete a Notification

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def notifications_id_put(request: web.Request, id, body) -> web.Response:
    """Update a Notification

    

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Notification.from_dict(body)
    return web.Response(status=200)


async def notifications_post(request: web.Request, body) -> web.Response:
    """Create a Notification

    

    :param body: 
    :type body: dict | bytes

    """
    body = Notification.from_dict(body)
    return web.Response(status=200)


async def notifications_test_post(request: web.Request, ) -> web.Response:
    """Send test notification to current user via Email and SMS

    


    """
    return web.Response(status=200)


async def notifications_types_get(request: web.Request, ) -> web.Response:
    """Fetch a list of available Notification types

    


    """
    return web.Response(status=200)
