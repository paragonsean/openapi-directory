from typing import List, Dict
from aiohttp import web

from openapi_server.models.notification_count import NotificationCount
from openapi_server.models.notification_thread import NotificationThread
from openapi_server import util


async def notify_get_list(request: web.Request, all=None, status_types=None, subject_type=None, since=None, before=None, page=None, limit=None) -> web.Response:
    """List users&#39;s notification threads

    

    :param all: If true, show notifications marked as read. Default value is false
    :type all: bool
    :param status_types: Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread &amp; pinned.
    :type status_types: List[str]
    :param subject_type: filter notifications by subject type
    :type subject_type: List[str]
    :param since: Only show notifications updated after the given time. This is a timestamp in RFC 3339 format
    :type since: str
    :param before: Only show notifications updated before the given time. This is a timestamp in RFC 3339 format
    :type before: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    since = util.deserialize_datetime(since)
    before = util.deserialize_datetime(before)
    return web.Response(status=200)


async def notify_get_repo_list(request: web.Request, owner, repo, all=None, status_types=None, subject_type=None, since=None, before=None, page=None, limit=None) -> web.Response:
    """List users&#39;s notification threads on a specific repo

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param all: If true, show notifications marked as read. Default value is false
    :type all: bool
    :param status_types: Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread &amp; pinned
    :type status_types: List[str]
    :param subject_type: filter notifications by subject type
    :type subject_type: List[str]
    :param since: Only show notifications updated after the given time. This is a timestamp in RFC 3339 format
    :type since: str
    :param before: Only show notifications updated before the given time. This is a timestamp in RFC 3339 format
    :type before: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    since = util.deserialize_datetime(since)
    before = util.deserialize_datetime(before)
    return web.Response(status=200)


async def notify_get_thread(request: web.Request, id) -> web.Response:
    """Get notification thread by ID

    

    :param id: id of notification thread
    :type id: str

    """
    return web.Response(status=200)


async def notify_new_available(request: web.Request, ) -> web.Response:
    """Check if unread notifications exist

    


    """
    return web.Response(status=200)


async def notify_read_list(request: web.Request, last_read_at=None, all=None, status_types=None, to_status=None) -> web.Response:
    """Mark notification threads as read, pinned or unread

    

    :param last_read_at: Describes the last point that notifications were checked. Anything updated since this time will not be updated.
    :type last_read_at: str
    :param all: If true, mark all notifications on this repo. Default value is false
    :type all: str
    :param status_types: Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread.
    :type status_types: List[str]
    :param to_status: Status to mark notifications as, Defaults to read.
    :type to_status: str

    """
    last_read_at = util.deserialize_datetime(last_read_at)
    return web.Response(status=200)


async def notify_read_repo_list(request: web.Request, owner, repo, all=None, status_types=None, to_status=None, last_read_at=None) -> web.Response:
    """Mark notification threads as read, pinned or unread on a specific repo

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str
    :param all: If true, mark all notifications on this repo. Default value is false
    :type all: str
    :param status_types: Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread.
    :type status_types: List[str]
    :param to_status: Status to mark notifications as. Defaults to read.
    :type to_status: str
    :param last_read_at: Describes the last point that notifications were checked. Anything updated since this time will not be updated.
    :type last_read_at: str

    """
    last_read_at = util.deserialize_datetime(last_read_at)
    return web.Response(status=200)


async def notify_read_thread(request: web.Request, id, to_status=None) -> web.Response:
    """Mark notification thread as read by ID

    

    :param id: id of notification thread
    :type id: str
    :param to_status: Status to mark notifications as
    :type to_status: str

    """
    return web.Response(status=200)
