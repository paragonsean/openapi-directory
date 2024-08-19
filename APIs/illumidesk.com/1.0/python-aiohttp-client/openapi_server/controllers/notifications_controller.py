from typing import List, Dict
from aiohttp import web

from openapi_server.models.not_found import NotFound
from openapi_server.models.notification import Notification
from openapi_server.models.notification_error import NotificationError
from openapi_server.models.notification_list_update_data import NotificationListUpdateData
from openapi_server.models.notification_settings import NotificationSettings
from openapi_server.models.notification_settings_data import NotificationSettingsData
from openapi_server.models.notification_settings_error import NotificationSettingsError
from openapi_server.models.notification_update_data import NotificationUpdateData
from openapi_server import util


async def notification_read(request: web.Request, namespace, notification_id) -> web.Response:
    """Retrieve a specific notification.

    

    :param namespace: User or team data.
    :type namespace: str
    :param notification_id: Notification UUID.
    :type notification_id: str

    """
    return web.Response(status=200)


async def notification_settings_create(request: web.Request, namespace, notification_settings_data) -> web.Response:
    """Create global notification settings

    

    :param namespace: User or team name.
    :type namespace: str
    :param notification_settings_data: 
    :type notification_settings_data: dict | bytes

    """
    notification_settings_data = NotificationSettingsData.from_dict(notification_settings_data)
    return web.Response(status=200)


async def notification_settings_entity_create(request: web.Request, namespace, entity, notification_settings_data=None) -> web.Response:
    """Create global notification settings

    

    :param namespace: User or team name.
    :type namespace: str
    :param entity: Entity whose settings should be retrieved.
    :type entity: str
    :param notification_settings_data: 
    :type notification_settings_data: dict | bytes

    """
    notification_settings_data = NotificationSettingsData.from_dict(notification_settings_data)
    return web.Response(status=200)


async def notification_settings_entity_read(request: web.Request, namespace, entity) -> web.Response:
    """Retrieve global notification settings for the authenticated user

    

    :param namespace: User or team data.
    :type namespace: str
    :param entity: Entity whose settings should be retrieved.
    :type entity: str

    """
    return web.Response(status=200)


async def notification_settings_entity_update(request: web.Request, namespace, entity, notification_settings_data=None) -> web.Response:
    """Modify global notification settings.

    

    :param namespace: User or team name.
    :type namespace: str
    :param entity: Entity whose settings should be retrieved.
    :type entity: str
    :param notification_settings_data: 
    :type notification_settings_data: dict | bytes

    """
    notification_settings_data = NotificationSettingsData.from_dict(notification_settings_data)
    return web.Response(status=200)


async def notification_settings_read(request: web.Request, namespace) -> web.Response:
    """Retrieve global notification settings for the authenticated user

    

    :param namespace: User or team data.
    :type namespace: str

    """
    return web.Response(status=200)


async def notification_settings_update(request: web.Request, namespace, notification_settings_data=None) -> web.Response:
    """Modify global notification settings.

    

    :param namespace: User or team name.
    :type namespace: str
    :param notification_settings_data: 
    :type notification_settings_data: dict | bytes

    """
    notification_settings_data = NotificationSettingsData.from_dict(notification_settings_data)
    return web.Response(status=200)


async def notification_update(request: web.Request, namespace, notification_id, notification_data=None) -> web.Response:
    """Mark a specific notification as either read or unread.

    

    :param namespace: User or team data.
    :type namespace: str
    :param notification_id: Notification UUID.
    :type notification_id: str
    :param notification_data: 
    :type notification_data: dict | bytes

    """
    notification_data = NotificationUpdateData.from_dict(notification_data)
    return web.Response(status=200)


async def notifications_list(request: web.Request, namespace, limit=None, offset=None, ordering=None, read=None) -> web.Response:
    """Get notifications of all types and entities for the authenticated user.

    

    :param namespace: User or team data.
    :type namespace: str
    :param limit: Limit when getting items.
    :type limit: str
    :param offset: Offset when getting items.
    :type offset: str
    :param ordering: Ordering when getting items.
    :type ordering: str
    :param read: When true, get only read notifications. When false, get only unread notifications. Default behavior is to return both read and unread.
    :type read: bool

    """
    return web.Response(status=200)


async def notifications_list_entity(request: web.Request, namespace, entity, limit=None, offset=None, ordering=None, read=None) -> web.Response:
    """Get notifications of all types and entities for the authenticated user.

    

    :param namespace: User or team data.
    :type namespace: str
    :param entity: Entity to filter notifications by.
    :type entity: str
    :param limit: Limit when getting items.
    :type limit: str
    :param offset: Offset when getting items.
    :type offset: str
    :param ordering: Ordering when getting items.
    :type ordering: str
    :param read: When true, get only read notifications. When false, get only unread notifications. Default behavior is to return both read and unread.
    :type read: bool

    """
    return web.Response(status=200)


async def notifications_update_entity_list(request: web.Request, namespace, entity, notification_data) -> web.Response:
    """Mark a list of notifications as either read or unread.

    

    :param namespace: User or team name.
    :type namespace: str
    :param entity: Entity to filter notifications by.
    :type entity: str
    :param notification_data: 
    :type notification_data: dict | bytes

    """
    notification_data = NotificationListUpdateData.from_dict(notification_data)
    return web.Response(status=200)


async def notifications_update_list(request: web.Request, namespace, notification_data) -> web.Response:
    """Mark a list of notifications as either read or unread.

    

    :param namespace: User or team name.
    :type namespace: str
    :param notification_data: 
    :type notification_data: dict | bytes

    """
    notification_data = NotificationListUpdateData.from_dict(notification_data)
    return web.Response(status=200)
