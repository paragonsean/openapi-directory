from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.ban_request import BanRequest
from openapi_server.models.create_block_list_request import CreateBlockListRequest
from openapi_server.models.deactivate_user_request import DeactivateUserRequest
from openapi_server.models.deactivate_user_response import DeactivateUserResponse
from openapi_server.models.deactivate_users_request import DeactivateUsersRequest
from openapi_server.models.deactivate_users_response import DeactivateUsersResponse
from openapi_server.models.delete_user_response import DeleteUserResponse
from openapi_server.models.delete_users_request import DeleteUsersRequest
from openapi_server.models.delete_users_response import DeleteUsersResponse
from openapi_server.models.flag_request import FlagRequest
from openapi_server.models.flag_response import FlagResponse
from openapi_server.models.get_block_list_response import GetBlockListResponse
from openapi_server.models.list_block_list_response import ListBlockListResponse
from openapi_server.models.mute_user_request import MuteUserRequest
from openapi_server.models.mute_user_response import MuteUserResponse
from openapi_server.models.query_banned_users_request import QueryBannedUsersRequest
from openapi_server.models.query_banned_users_response import QueryBannedUsersResponse
from openapi_server.models.query_message_flags_request import QueryMessageFlagsRequest
from openapi_server.models.query_message_flags_response import QueryMessageFlagsResponse
from openapi_server.models.reactivate_user_request import ReactivateUserRequest
from openapi_server.models.reactivate_user_response import ReactivateUserResponse
from openapi_server.models.reactivate_users_request import ReactivateUsersRequest
from openapi_server.models.reactivate_users_response import ReactivateUsersResponse
from openapi_server.models.response import Response
from openapi_server.models.unmute_response import UnmuteResponse
from openapi_server.models.unmute_user_request import UnmuteUserRequest
from openapi_server.models.update_block_list_request import UpdateBlockListRequest
from openapi_server import util


async def ban_0(request: web.Request, body) -> web.Response:
    """Ban user

    Restricts user activity either in specific channel or globally  Sends events: - user.banned  Required permissions: - BanChannelMember - BanUser 

    :param body: 
    :type body: dict | bytes

    """
    body = BanRequest.from_dict(body)
    return web.Response(status=200)


async def create_block_list_0(request: web.Request, body) -> web.Response:
    """Create block list

    Creates a new application blocklist, once created the blocklist can be used by any channel type 

    :param body: Block list
    :type body: dict | bytes

    """
    body = CreateBlockListRequest.from_dict(body)
    return web.Response(status=200)


async def deactivate_user_1(request: web.Request, user_id, body) -> web.Response:
    """Deactivate user

    Deactivates user with possibility to activate it back  Sends events: - user.deactivated 

    :param user_id: 
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeactivateUserRequest.from_dict(body)
    return web.Response(status=200)


async def deactivate_users_1(request: web.Request, body) -> web.Response:
    """Deactivate users

    Deactivate users in batches  Sends events: - user.deactivated 

    :param body: 
    :type body: dict | bytes

    """
    body = DeactivateUsersRequest.from_dict(body)
    return web.Response(status=200)


async def delete_block_list_0(request: web.Request, name) -> web.Response:
    """Delete block list

    Deletes previously created application blocklist 

    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def delete_user_1(request: web.Request, user_id, mark_messages_deleted=None, hard_delete=None, delete_conversation_channels=None) -> web.Response:
    """Delete user

    Deletes user and optionally all their belongings. The Endpoint is deprecated, please use &#39;Delete Users&#39; endpoint instead  Sends events: - channel.deleted - message.deleted - user.deleted 

    :param user_id: 
    :type user_id: str
    :param mark_messages_deleted: 
    :type mark_messages_deleted: bool
    :param hard_delete: 
    :type hard_delete: bool
    :param delete_conversation_channels: 
    :type delete_conversation_channels: bool

    """
    return web.Response(status=200)


async def delete_users_1(request: web.Request, body) -> web.Response:
    """Delete Users

    Deletes users and optionally all their belongings asynchronously.  Sends events: - channel.deleted - user.deleted 

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteUsersRequest.from_dict(body)
    return web.Response(status=200)


async def flag(request: web.Request, body) -> web.Response:
    """Flag

    Reports message or user for review by moderators  Sends events: - message.flagged - user.flagged  Required permissions: - FlagMessage - FlagUser 

    :param body: 
    :type body: dict | bytes

    """
    body = FlagRequest.from_dict(body)
    return web.Response(status=200)


async def get_block_list_0(request: web.Request, name) -> web.Response:
    """Get block list

    Returns block list by given name 

    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def list_block_lists_0(request: web.Request, ) -> web.Response:
    """List block lists

    Returns all available block lists 


    """
    return web.Response(status=200)


async def mute_user_0(request: web.Request, body) -> web.Response:
    """Mute user

    Mutes one or several users  Sends events: - user.muted  Required permissions: - MuteUser 

    :param body: 
    :type body: dict | bytes

    """
    body = MuteUserRequest.from_dict(body)
    return web.Response(status=200)


async def query_banned_users_0(request: web.Request, payload=None) -> web.Response:
    """Query Banned Users

    Find and filter channel scoped or global user bans  Required permissions: - ReadChannel 

    :param payload: 
    :type payload: dict | bytes

    """
    payload = .from_dict(payload)
    return web.Response(status=200)


async def query_message_flags_0(request: web.Request, payload=None) -> web.Response:
    """Query Message Flags

    Find and filter message flags  Required permissions: - ReadMessageFlags 

    :param payload: 
    :type payload: dict | bytes

    """
    payload = .from_dict(payload)
    return web.Response(status=200)


async def reactivate_user_1(request: web.Request, user_id, body) -> web.Response:
    """Reactivate user

    Activates user who&#39;s been deactivated previously  Sends events: - user.reactivated 

    :param user_id: 
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReactivateUserRequest.from_dict(body)
    return web.Response(status=200)


async def reactivate_users_1(request: web.Request, body) -> web.Response:
    """Reactivate users

    Reactivate users in batches  Sends events: - user.reactivated 

    :param body: 
    :type body: dict | bytes

    """
    body = ReactivateUsersRequest.from_dict(body)
    return web.Response(status=200)


async def unban_0(request: web.Request, target_user_id=None, type=None, id=None) -> web.Response:
    """Unban user

    Removes previously applied ban  Sends events: - user.unbanned  Required permissions: - BanChannelMember - BanUser 

    :param target_user_id: 
    :type target_user_id: str
    :param type: 
    :type type: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def unflag(request: web.Request, body) -> web.Response:
    """Unflag

    Removes previously created user or message flag  Required permissions: - FlagMessage - FlagUser 

    :param body: 
    :type body: dict | bytes

    """
    body = FlagRequest.from_dict(body)
    return web.Response(status=200)


async def unmute_user_0(request: web.Request, body) -> web.Response:
    """Unmute user

    Unmutes previously muted user  Sends events: - user.unmuted  Required permissions: - MuteUser 

    :param body: 
    :type body: dict | bytes

    """
    body = UnmuteUserRequest.from_dict(body)
    return web.Response(status=200)


async def update_block_list_0(request: web.Request, name, body) -> web.Response:
    """Update block list

    Updates contents of the block list 

    :param name: 
    :type name: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateBlockListRequest.from_dict(body)
    return web.Response(status=200)
