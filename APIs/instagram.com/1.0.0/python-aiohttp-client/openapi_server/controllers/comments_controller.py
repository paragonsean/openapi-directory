from typing import List, Dict
from aiohttp import web

from openapi_server.models.comments_response import CommentsResponse
from openapi_server.models.status_response import StatusResponse
from openapi_server import util


async def media_media_id_comments_comment_id_delete(request: web.Request, media_id, comment_id) -> web.Response:
    """Remove a comment.

    Remove a comment either on the authenticated user&#39;s media object or authored by the authenticated user. 

    :param media_id: The ID of the media resource.
    :type media_id: str
    :param comment_id: The ID of the comment entry.
    :type comment_id: str

    """
    return web.Response(status=200)


async def media_media_id_comments_get(request: web.Request, media_id) -> web.Response:
    """Get a list of recent comments on a media object.

    Get a list of recent comments on a media object.

    :param media_id: The ID of the media resource.
    :type media_id: str

    """
    return web.Response(status=200)


async def media_media_id_comments_post(request: web.Request, media_id, text) -> web.Response:
    """Create a comment on a media object.

    Create a comment on a media object with the following rules:    * The total length of the comment cannot exceed 300 characters.   * The comment cannot contain more than 4 hashtags.   * The comment cannot contain more than 1 URL.   * The comment cannot consist of all capital letters. 

    :param media_id: The ID of the media resource.
    :type media_id: str
    :param text: Text to post as a comment on the media object as specified in &#x60;media-id&#x60;.
    :type text: str

    """
    return web.Response(status=200)
