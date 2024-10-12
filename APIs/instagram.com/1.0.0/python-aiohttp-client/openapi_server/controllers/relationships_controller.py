from typing import List, Dict
from aiohttp import web

from openapi_server.models.relationship_post_response import RelationshipPostResponse
from openapi_server.models.relationship_response import RelationshipResponse
from openapi_server.models.users_info_response import UsersInfoResponse
from openapi_server.models.users_paging_response import UsersPagingResponse
from openapi_server import util


async def users_self_requested_by_get(request: web.Request, ) -> web.Response:
    """List the users who have requested this user&#39;s permission to follow.

    List the users who have requested this user&#39;s permission to follow.


    """
    return web.Response(status=200)


async def users_user_id_followed_by_get(request: web.Request, user_id) -> web.Response:
    """Get the list of users this user is followed by.

    Get the list of users this user is followed by. To get users followed by the owner of the access token, you can use **self** instead of the &#x60;user-id&#x60;. 

    :param user_id: The ID of a user, or **self** to retrieve information about authenticated user.
    :type user_id: str

    """
    return web.Response(status=200)


async def users_user_id_follows_get(request: web.Request, user_id) -> web.Response:
    """Get the list of users this user follows.

    Get the list of users this user follows. To get follows of the owner of the access token, you can use **self** instead of the &#x60;user-id&#x60;. 

    :param user_id: The ID of a user, or **self** to retrieve information about authenticated user.
    :type user_id: str

    """
    return web.Response(status=200)


async def users_user_id_relationship_get(request: web.Request, user_id) -> web.Response:
    """Get information about a relationship to another user.

    Get information about a relationship to another user.

    :param user_id: The ID of a user to get information about.
    :type user_id: str

    """
    return web.Response(status=200)


async def users_user_id_relationship_post(request: web.Request, user_id, action) -> web.Response:
    """Modify the relationship between the current user and the target user.

    Modify the relationship between the current user and the target user.

    :param user_id: The ID of the target user.
    :type user_id: str
    :param action: Type of action to apply for relationship with the user.
    :type action: str

    """
    return web.Response(status=200)
