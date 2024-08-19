from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.invite_user_request import InviteUserRequest
from openapi_server.models.join_account_request import JoinAccountRequest
from openapi_server.models.session_model import SessionModel
from openapi_server.models.user_account import UserAccount
from openapi_server.models.user_account_roles_results import UserAccountRolesResults
from openapi_server.models.user_invitation_model import UserInvitationModel
from openapi_server import util


async def cancel_user_invitation(request: web.Request, user_invitation_id) -> web.Response:
    """Cancel user invitation

    

    :param user_invitation_id: User Invitation ID
    :type user_invitation_id: str

    """
    return web.Response(status=200)


async def delete_user(request: web.Request, user_id) -> web.Response:
    """Delete user

    

    :param user_id: User ID
    :type user_id: int

    """
    return web.Response(status=200)


async def get_user(request: web.Request, user_id) -> web.Response:
    """Get user

    

    :param user_id: User ID
    :type user_id: int

    """
    return web.Response(status=200)


async def get_user_invitations(request: web.Request, ) -> web.Response:
    """Get user invitations

    


    """
    return web.Response(status=200)


async def get_users(request: web.Request, ) -> web.Response:
    """Get users

    


    """
    return web.Response(status=200)


async def invite_user(request: web.Request, body) -> web.Response:
    """Invite user

    

    :param body: 
    :type body: dict | bytes

    """
    body = InviteUserRequest.from_dict(body)
    return web.Response(status=200)


async def join_account(request: web.Request, body) -> web.Response:
    """Join Account

    

    :param body: 
    :type body: dict | bytes

    """
    body = JoinAccountRequest.from_dict(body)
    return web.Response(status=200)


async def update_user(request: web.Request, body) -> web.Response:
    """Update user

    

    :param body: 
    :type body: dict | bytes

    """
    body = UserAccount.from_dict(body)
    return web.Response(status=200)
