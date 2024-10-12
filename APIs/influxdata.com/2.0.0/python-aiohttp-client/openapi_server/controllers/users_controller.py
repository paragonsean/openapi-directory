from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.password_reset_body import PasswordResetBody
from openapi_server.models.user import User
from openapi_server.models.user_response import UserResponse
from openapi_server.models.users import Users
from openapi_server import util


async def delete_users_id(request: web.Request, user_id, zap_trace_span=None) -> web.Response:
    """Delete a user

    

    :param user_id: The ID of the user to delete.
    :type user_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_flags(request: web.Request, zap_trace_span=None) -> web.Response:
    """Return the feature flags for the currently authenticated user

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_me(request: web.Request, zap_trace_span=None) -> web.Response:
    """Retrieve the currently authenticated user

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_users(request: web.Request, zap_trace_span=None, offset=None, limit=None, after=None, name=None, id=None) -> web.Response:
    """List all users

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int
    :param after: The last resource ID from which to seek from (but not including). This is to be used instead of &#x60;offset&#x60;. 
    :type after: str
    :param name: 
    :type name: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_users_id(request: web.Request, user_id, zap_trace_span=None) -> web.Response:
    """Retrieve a user

    

    :param user_id: The user ID.
    :type user_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def patch_users_id(request: web.Request, user_id, body, zap_trace_span=None) -> web.Response:
    """Update a user

    

    :param user_id: The ID of the user to update.
    :type user_id: str
    :param body: User update to apply
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = User.from_dict(body)
    return web.Response(status=200)


async def post_users(request: web.Request, body, zap_trace_span=None) -> web.Response:
    """Create a user

    

    :param body: User to create
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = User.from_dict(body)
    return web.Response(status=200)


async def post_users_id_password(request: web.Request, user_id, body, zap_trace_span=None) -> web.Response:
    """Update a password

    

    :param user_id: The user ID.
    :type user_id: str
    :param body: New password
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = PasswordResetBody.from_dict(body)
    return web.Response(status=200)


async def put_me_password(request: web.Request, body, zap_trace_span=None) -> web.Response:
    """Update a password

    

    :param body: New password
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = PasswordResetBody.from_dict(body)
    return web.Response(status=200)
