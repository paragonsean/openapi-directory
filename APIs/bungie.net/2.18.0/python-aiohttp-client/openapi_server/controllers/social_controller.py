from typing import List, Dict
from aiohttp import web

from openapi_server.models.group_v2_get_user_clan_invite_setting200_response import GroupV2GetUserClanInviteSetting200Response
from openapi_server.models.social_get_friend_list200_response import SocialGetFriendList200Response
from openapi_server.models.social_get_friend_request_list200_response import SocialGetFriendRequestList200Response
from openapi_server.models.social_get_platform_friend_list200_response import SocialGetPlatformFriendList200Response
from openapi_server import util


async def social_accept_friend_request(request: web.Request, membership_id) -> web.Response:
    """social_accept_friend_request

    Accepts a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.

    :param membership_id: The membership id of the user you wish to accept.
    :type membership_id: str

    """
    return web.Response(status=200)


async def social_decline_friend_request(request: web.Request, membership_id) -> web.Response:
    """social_decline_friend_request

    Declines a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.

    :param membership_id: The membership id of the user you wish to decline.
    :type membership_id: str

    """
    return web.Response(status=200)


async def social_get_friend_list(request: web.Request, ) -> web.Response:
    """social_get_friend_list

    Returns your Bungie Friend list


    """
    return web.Response(status=200)


async def social_get_friend_request_list(request: web.Request, ) -> web.Response:
    """social_get_friend_request_list

    Returns your friend request queue.


    """
    return web.Response(status=200)


async def social_get_platform_friend_list(request: web.Request, friend_platform, page) -> web.Response:
    """social_get_platform_friend_list

    Gets the platform friend of the requested type, with additional information if they have Bungie accounts. Must have a recent login session with said platform.

    :param friend_platform: The platform friend type.
    :type friend_platform: int
    :param page: The zero based page to return. Page size is 100.
    :type page: str

    """
    return web.Response(status=200)


async def social_issue_friend_request(request: web.Request, membership_id) -> web.Response:
    """social_issue_friend_request

    Requests a friend relationship with the target user. Any of the target user&#39;s linked membership ids are valid inputs.

    :param membership_id: The membership id of the user you wish to add.
    :type membership_id: str

    """
    return web.Response(status=200)


async def social_remove_friend(request: web.Request, membership_id) -> web.Response:
    """social_remove_friend

    Remove a friend relationship with the target user. The user must be on your friend list, though no error will occur if they are not.

    :param membership_id: The membership id of the user you wish to remove.
    :type membership_id: str

    """
    return web.Response(status=200)


async def social_remove_friend_request(request: web.Request, membership_id) -> web.Response:
    """social_remove_friend_request

    Remove a friend relationship with the target user. The user must be on your outgoing request friend list, though no error will occur if they are not.

    :param membership_id: The membership id of the user you wish to remove.
    :type membership_id: str

    """
    return web.Response(status=200)
