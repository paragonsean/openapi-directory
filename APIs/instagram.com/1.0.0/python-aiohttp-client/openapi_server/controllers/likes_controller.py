from typing import List, Dict
from aiohttp import web

from openapi_server.models.status_response import StatusResponse
from openapi_server.models.users_info_response import UsersInfoResponse
from openapi_server import util


async def media_media_id_likes_delete(request: web.Request, media_id) -> web.Response:
    """Remove a like on this media by the current user.

    Remove a like on this media by the currently authenticated user.

    :param media_id: The ID of the media resource.
    :type media_id: str

    """
    return web.Response(status=200)


async def media_media_id_likes_get(request: web.Request, media_id) -> web.Response:
    """Get a list of users who have liked this media.

    Get a list of users who have liked this media.

    :param media_id: The ID of the media resource.
    :type media_id: str

    """
    return web.Response(status=200)


async def media_media_id_likes_post(request: web.Request, media_id) -> web.Response:
    """Set a like on this media by the current user.

    Set a like on this media by the currently authenticated user.

    :param media_id: The ID of the media resource.
    :type media_id: str

    """
    return web.Response(status=200)
