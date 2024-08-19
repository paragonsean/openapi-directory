from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.offering_metadata_response import OfferingMetadataResponse
from openapi_server.models.suspended_request import SuspendedRequest
from openapi_server.models.user import User
from openapi_server.models.user_response import UserResponse
from openapi_server import util


async def users_post(request: web.Request, body) -> web.Response:
    """Add new user

    Creates a new user.

    :param body: user
    :type body: dict | bytes

    """
    body = User.from_dict(body)
    return web.Response(status=200)


async def users_user_email_get(request: web.Request, user_email) -> web.Response:
    """Find user by email

    Responds with a user matching the specified email.

    :param user_email: user&#39;s email
    :type user_email: str

    """
    return web.Response(status=200)


async def users_user_email_invite_email_post(request: web.Request, user_email) -> web.Response:
    """Resend invitation email

    Re-sends an invitation e-mail to the specified user.

    :param user_email: user&#39;s email
    :type user_email: str

    """
    return web.Response(status=200)


async def users_user_email_offerings_get(request: web.Request, user_email) -> web.Response:
    """Find user&#39;s offerings

    Responds with all offerings that the user in.

    :param user_email: user&#39;s email
    :type user_email: str

    """
    return web.Response(status=200)


async def users_user_email_offerings_post(request: web.Request, user_email, body) -> web.Response:
    """Adds the user to the specified offerings as a learner

    Adds a user to an array of offerings by offeringId.

    :param user_email: user&#39;s email
    :type user_email: str
    :param body: offering ids
    :type body: List[str]

    """
    return web.Response(status=200)


async def users_user_email_patch(request: web.Request, user_email, body=None) -> web.Response:
    """Update user

    Updates the specified user by email.

    :param user_email: user&#39;s email
    :type user_email: str
    :param body: 
    :type body: dict | bytes

    """
    body = User.from_dict(body)
    return web.Response(status=200)


async def users_user_email_permissions_permission_name_post(request: web.Request, user_email, permission_name) -> web.Response:
    """Add permission to user

    Adds additional permissions to the specified user.

    :param user_email: user&#39;s email
    :type user_email: str
    :param permission_name: permission name
    :type permission_name: str

    """
    return web.Response(status=200)


async def users_user_email_suspend_put(request: web.Request, user_email, body) -> web.Response:
    """Suspend user

    Suspends the specified user&#39;s account.

    :param user_email: user&#39;s email
    :type user_email: str
    :param body: 
    :type body: dict | bytes

    """
    body = SuspendedRequest.from_dict(body)
    return web.Response(status=200)
