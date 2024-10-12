from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error import DefaultError
from openapi_server.models.error_entity import ErrorEntity
from openapi_server.models.metadata_patch import MetadataPatch
from openapi_server.models.notification import Notification
from openapi_server.models.notification_created import NotificationCreated
from openapi_server.models.notification_item import NotificationItem
from openapi_server.models.notification_new import NotificationNew
from openapi_server.models.notification_patch import NotificationPatch
from openapi_server import util


async def notification_delete(request: web.Request, notification_id) -> web.Response:
    """Delete a Notification

    Delete a *Notification*. 

    :param notification_id: Unique identifier of a *Notification*.
    :type notification_id: str

    """
    return web.Response(status=200)


async def notification_get_metadata(request: web.Request, notification_id) -> web.Response:
    """List metadata

    Get the metadata of the *Notification*.

    :param notification_id: Unique identifier of a *Notification*.
    :type notification_id: str

    """
    return web.Response(status=200)


async def notification_patch(request: web.Request, notification_id, notification_patch) -> web.Response:
    """Modify a Notification

    Modify a *Notification*. 

    :param notification_id: Unique identifier of a *Notification*.
    :type notification_id: str
    :param notification_patch: 
    :type notification_patch: dict | bytes

    """
    notification_patch = NotificationPatch.from_dict(notification_patch)
    return web.Response(status=200)


async def notification_patch_metadata(request: web.Request, notification_id, metadata_patch) -> web.Response:
    """Modify metadata of a Notification

    Modify the metadata of a *Notification*. Keys are limited to the same format as tags (up to 21 characters, [a-z0-9], starting with [a-z]). Values can be any JSON value. 

    :param notification_id: Unique identifier of a *Notification*.
    :type notification_id: str
    :param metadata_patch: Modifications to apply to the metadata of the resource. 
    :type metadata_patch: dict | bytes

    """
    metadata_patch = MetadataPatch.from_dict(metadata_patch)
    return web.Response(status=200)


async def notifications_get(request: web.Request, notification_id) -> web.Response:
    """Information about a Notification

    Get information about a *Notification*. 

    :param notification_id: Unique identifier of a *Notification*.
    :type notification_id: str

    """
    return web.Response(status=200)


async def place_new_notification(request: web.Request, place_id, notification) -> web.Response:
    """Create a Notification

    Create a new *Notification*.

    :param place_id: Unique identifier of a *Place*.
    :type place_id: str
    :param notification: 
    :type notification: dict | bytes

    """
    notification = NotificationNew.from_dict(notification)
    return web.Response(status=200)


async def place_notifications(request: web.Request, place_id, embed_metadata=None) -> web.Response:
    """List Notifications

    Get the list of *Notifications* available in this *Place*.

    :param place_id: Unique identifier of a *Place*.
    :type place_id: str
    :param embed_metadata: Request to include the given keys of metadata in the response. If a key doesn&#39;t exist on the resource it is ignored. **Note:** This only applies to the top level resources. 
    :type embed_metadata: List[str]

    """
    return web.Response(status=200)
