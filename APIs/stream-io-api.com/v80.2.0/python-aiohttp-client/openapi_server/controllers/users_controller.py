from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.ban_request import BanRequest
from openapi_server.models.connect_request import ConnectRequest
from openapi_server.models.deactivate_user_request import DeactivateUserRequest
from openapi_server.models.deactivate_user_response import DeactivateUserResponse
from openapi_server.models.deactivate_users_request import DeactivateUsersRequest
from openapi_server.models.deactivate_users_response import DeactivateUsersResponse
from openapi_server.models.delete_user_response import DeleteUserResponse
from openapi_server.models.delete_users_request import DeleteUsersRequest
from openapi_server.models.delete_users_response import DeleteUsersResponse
from openapi_server.models.export_user_response import ExportUserResponse
from openapi_server.models.export_users_request import ExportUsersRequest
from openapi_server.models.export_users_response import ExportUsersResponse
from openapi_server.models.flag_request import FlagRequest
from openapi_server.models.flag_response import FlagResponse
from openapi_server.models.guest_request import GuestRequest
from openapi_server.models.guest_response import GuestResponse
from openapi_server.models.mute_user_request import MuteUserRequest
from openapi_server.models.mute_user_response import MuteUserResponse
from openapi_server.models.query_banned_users_request import QueryBannedUsersRequest
from openapi_server.models.query_banned_users_response import QueryBannedUsersResponse
from openapi_server.models.query_users_request import QueryUsersRequest
from openapi_server.models.reactivate_user_request import ReactivateUserRequest
from openapi_server.models.reactivate_user_response import ReactivateUserResponse
from openapi_server.models.reactivate_users_request import ReactivateUsersRequest
from openapi_server.models.reactivate_users_response import ReactivateUsersResponse
from openapi_server.models.response import Response
from openapi_server.models.restore_users_request import RestoreUsersRequest
from openapi_server.models.unmute_response import UnmuteResponse
from openapi_server.models.unmute_user_request import UnmuteUserRequest
from openapi_server.models.update_user_partial_request import UpdateUserPartialRequest
from openapi_server.models.update_users_request import UpdateUsersRequest
from openapi_server.models.update_users_response import UpdateUsersResponse
from openapi_server.models.users_response import UsersResponse
from openapi_server import util


async def ban(request: web.Request, body) -> web.Response:
    """Ban user

    Restricts user activity either in specific channel or globally  Sends events: - user.banned  Required permissions: - BanChannelMember - BanUser 

    :param body: 
    :type body: dict | bytes

    """
    body = BanRequest.from_dict(body)
    return web.Response(status=200)


async def connect(request: web.Request, _json=None) -> web.Response:
    """Connect (WebSocket)

    Establishes WebSocket connection for user  Sends events: - user.updated 

    :param _json: 
    :type _json: dict | bytes

    """
    _json = .from_dict(_json)
    return web.Response(status=200)


async def create_guest(request: web.Request, body) -> web.Response:
    """Create guest

    Creates guest user 

    :param body: 
    :type body: dict | bytes

    """
    body = GuestRequest.from_dict(body)
    return web.Response(status=200)


async def deactivate_user(request: web.Request, user_id, body) -> web.Response:
    """Deactivate user

    Deactivates user with possibility to activate it back  Sends events: - user.deactivated 

    :param user_id: 
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeactivateUserRequest.from_dict(body)
    return web.Response(status=200)


async def deactivate_users(request: web.Request, body) -> web.Response:
    """Deactivate users

    Deactivate users in batches  Sends events: - user.deactivated 

    :param body: 
    :type body: dict | bytes

    """
    body = DeactivateUsersRequest.from_dict(body)
    return web.Response(status=200)


async def delete_user(request: web.Request, user_id, mark_messages_deleted=None, hard_delete=None, delete_conversation_channels=None) -> web.Response:
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


async def delete_users(request: web.Request, body) -> web.Response:
    """Delete Users

    Deletes users and optionally all their belongings asynchronously.  Sends events: - channel.deleted - user.deleted 

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteUsersRequest.from_dict(body)
    return web.Response(status=200)


async def export_user(request: web.Request, body) -> web.Response:
    """Export users

    Exports user profile, reactions and messages for list of given users 

    :param body: 
    :type body: dict | bytes

    """
    body = ExportUsersRequest.from_dict(body)
    return web.Response(status=200)


async def flag_1(request: web.Request, body) -> web.Response:
    """Flag

    Reports message or user for review by moderators  Sends events: - message.flagged - user.flagged  Required permissions: - FlagMessage - FlagUser 

    :param body: 
    :type body: dict | bytes

    """
    body = FlagRequest.from_dict(body)
    return web.Response(status=200)


async def long_poll(request: web.Request, _json=None, connection_id=None) -> web.Response:
    """Long Poll (Transport)

    WebSocket fallback transport endpoint  Sends events: - user.updated 

    :param _json: 
    :type _json: dict | bytes
    :param connection_id: 
    :type connection_id: str

    """
    _json = .from_dict(_json)
    return web.Response(status=200)


async def mute_user(request: web.Request, body) -> web.Response:
    """Mute user

    Mutes one or several users  Sends events: - user.muted  Required permissions: - MuteUser 

    :param body: 
    :type body: dict | bytes

    """
    body = MuteUserRequest.from_dict(body)
    return web.Response(status=200)


async def query_banned_users(request: web.Request, payload=None) -> web.Response:
    """Query Banned Users

    Find and filter channel scoped or global user bans  Required permissions: - ReadChannel 

    :param payload: 
    :type payload: dict | bytes

    """
    payload = .from_dict(payload)
    return web.Response(status=200)


async def query_users(request: web.Request, payload=None) -> web.Response:
    """Query users

    Find and filter users  Required permissions: - SearchUser 

    :param payload: 
    :type payload: dict | bytes

    """
    payload = .from_dict(payload)
    return web.Response(status=200)


async def reactivate_user(request: web.Request, user_id, body) -> web.Response:
    """Reactivate user

    Activates user who&#39;s been deactivated previously  Sends events: - user.reactivated 

    :param user_id: 
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReactivateUserRequest.from_dict(body)
    return web.Response(status=200)


async def reactivate_users(request: web.Request, body) -> web.Response:
    """Reactivate users

    Reactivate users in batches  Sends events: - user.reactivated 

    :param body: 
    :type body: dict | bytes

    """
    body = ReactivateUsersRequest.from_dict(body)
    return web.Response(status=200)


async def restore_users(request: web.Request, body) -> web.Response:
    """Restore users

    Restore soft deleted users 

    :param body: 
    :type body: dict | bytes

    """
    body = RestoreUsersRequest.from_dict(body)
    return web.Response(status=200)


async def unban(request: web.Request, target_user_id=None, type=None, id=None) -> web.Response:
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


async def unflag_1(request: web.Request, body) -> web.Response:
    """Unflag

    Removes previously created user or message flag  Required permissions: - FlagMessage - FlagUser 

    :param body: 
    :type body: dict | bytes

    """
    body = FlagRequest.from_dict(body)
    return web.Response(status=200)


async def unmute_user(request: web.Request, body) -> web.Response:
    """Unmute user

    Unmutes previously muted user  Sends events: - user.unmuted  Required permissions: - MuteUser 

    :param body: 
    :type body: dict | bytes

    """
    body = UnmuteUserRequest.from_dict(body)
    return web.Response(status=200)


async def update_users(request: web.Request, body) -> web.Response:
    """Upsert users

    Update or create users in bulk  Sends events: - user.updated 

    :param body: 
    :type body: dict | bytes

    """
    body = UpdateUsersRequest.from_dict(body)
    return web.Response(status=200)


async def update_users_partial(request: web.Request, body) -> web.Response:
    """Partially update user

    Updates certain fields of the user  Sends events: - user.presence.changed - user.updated 

    :param body: 
    :type body: dict | bytes

    """
    body = UpdateUserPartialRequest.from_dict(body)
    return web.Response(status=200)


async def users_user_id_export_get(request: web.Request, user_id) -> web.Response:
    """Export user

    Exports the user&#39;s profile, reactions and messages. Raises an error if a user has more than 10k messages or reactions 

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)
