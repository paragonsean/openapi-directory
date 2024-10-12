from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.deactivate_user_request import DeactivateUserRequest
from openapi_server.models.deactivate_user_response import DeactivateUserResponse
from openapi_server.models.deactivate_users_request import DeactivateUsersRequest
from openapi_server.models.deactivate_users_response import DeactivateUsersResponse
from openapi_server.models.delete_channels_request import DeleteChannelsRequest
from openapi_server.models.delete_channels_response import DeleteChannelsResponse
from openapi_server.models.delete_user_response import DeleteUserResponse
from openapi_server.models.delete_users_request import DeleteUsersRequest
from openapi_server.models.delete_users_response import DeleteUsersResponse
from openapi_server.models.reactivate_user_request import ReactivateUserRequest
from openapi_server.models.reactivate_user_response import ReactivateUserResponse
from openapi_server.models.reactivate_users_request import ReactivateUsersRequest
from openapi_server.models.reactivate_users_response import ReactivateUsersResponse
from openapi_server import util


async def deactivate_user_0(request: web.Request, user_id, body) -> web.Response:
    """Deactivate user

    Deactivates user with possibility to activate it back  Sends events: - user.deactivated 

    :param user_id: 
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeactivateUserRequest.from_dict(body)
    return web.Response(status=200)


async def deactivate_users_0(request: web.Request, body) -> web.Response:
    """Deactivate users

    Deactivate users in batches  Sends events: - user.deactivated 

    :param body: 
    :type body: dict | bytes

    """
    body = DeactivateUsersRequest.from_dict(body)
    return web.Response(status=200)


async def delete_channels_0(request: web.Request, body) -> web.Response:
    """Deletes channels asynchronously

    Allows to delete several channels at once asynchronously  Sends events: - channel.deleted  Required permissions: - DeleteChannel 

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteChannelsRequest.from_dict(body)
    return web.Response(status=200)


async def delete_user_0(request: web.Request, user_id, mark_messages_deleted=None, hard_delete=None, delete_conversation_channels=None) -> web.Response:
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


async def delete_users_0(request: web.Request, body) -> web.Response:
    """Delete Users

    Deletes users and optionally all their belongings asynchronously.  Sends events: - channel.deleted - user.deleted 

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteUsersRequest.from_dict(body)
    return web.Response(status=200)


async def reactivate_user_0(request: web.Request, user_id, body) -> web.Response:
    """Reactivate user

    Activates user who&#39;s been deactivated previously  Sends events: - user.reactivated 

    :param user_id: 
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReactivateUserRequest.from_dict(body)
    return web.Response(status=200)


async def reactivate_users_0(request: web.Request, body) -> web.Response:
    """Reactivate users

    Reactivate users in batches  Sends events: - user.reactivated 

    :param body: 
    :type body: dict | bytes

    """
    body = ReactivateUsersRequest.from_dict(body)
    return web.Response(status=200)
