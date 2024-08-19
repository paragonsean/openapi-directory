from typing import List, Dict
from aiohttp import web

from openapi_server.models.media_list_response import MediaListResponse
from openapi_server.models.user_response import UserResponse
from openapi_server.models.users_info_response import UsersInfoResponse
from openapi_server import util


async def users_search_get(request: web.Request, q, count=None) -> web.Response:
    """Search for a user by name.

    Search for a user by name.

    :param q: A query string.
    :type q: str
    :param count: Number of users to return.
    :type count: int

    """
    return web.Response(status=200)


async def users_self_feed_get(request: web.Request, count=None, min_id=None, max_id=None) -> web.Response:
    """See the authenticated user&#39;s feed.

    See the authenticated user&#39;s feed.  **Warning:** [Deprecated](http://instagram.com/developer/changelog/) for Apps created **on or after** Nov 17, 2015 

    :param count: Count of media to return.
    :type count: int
    :param min_id: Return media later than this &#x60;min_id&#x60;.
    :type min_id: str
    :param max_id: Return media earlier than this &#x60;max_id&#x60;.
    :type max_id: str

    """
    return web.Response(status=200)


async def users_self_media_liked_get(request: web.Request, count=None, max_like_id=None) -> web.Response:
    """See the list of media liked by the authenticated user.

    See the list of media liked by the authenticated user. Private media is returned as long as the authenticated user has permission to view that media. Liked media lists are only available for the currently authenticated user. 

    :param count: Count of media to return.
    :type count: int
    :param max_like_id: Return media liked before this id.
    :type max_like_id: str

    """
    return web.Response(status=200)


async def users_user_id_get(request: web.Request, user_id) -> web.Response:
    """Get basic information about a user.

    Get basic information about a user. To get information about the owner of the access token, you can use **self** instead of the &#x60;user-id&#x60;.  Security scope &#x60;public_content&#x60; is required to read information about other users. 

    :param user_id: The ID of a user to get information about, or **self** to retrieve information about authenticated user.
    :type user_id: str

    """
    return web.Response(status=200)


async def users_user_id_media_recent_get(request: web.Request, user_id, count=None, max_timestamp=None, min_timestamp=None, min_id=None, max_id=None) -> web.Response:
    """Get the most recent media published by a user.

    Get the most recent media published by a user. To get the most recent media published by the owner of the access token, you can use **self** instead of the &#x60;user-id&#x60;.  Security scope &#x60;public_content&#x60; is required to read information about other users. 

    :param user_id: The ID of a user to get recent media of, or **self** to retrieve media of authenticated user.
    :type user_id: str
    :param count: Count of media to return.
    :type count: int
    :param max_timestamp: Return media before this UNIX timestamp.
    :type max_timestamp: int
    :param min_timestamp: Return media after this UNIX timestamp.
    :type min_timestamp: int
    :param min_id: Return media later than this &#x60;min_id&#x60;.
    :type min_id: str
    :param max_id: Return media earlier than this &#x60;max_id&#x60;.
    :type max_id: str

    """
    return web.Response(status=200)
