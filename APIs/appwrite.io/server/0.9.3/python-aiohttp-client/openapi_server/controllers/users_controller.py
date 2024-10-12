from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_update_prefs_request import AccountUpdatePrefsRequest
from openapi_server.models.log_list import LogList
from openapi_server.models.session_list import SessionList
from openapi_server.models.user import User
from openapi_server.models.user_list import UserList
from openapi_server.models.users_create_request import UsersCreateRequest
from openapi_server.models.users_update_status_request import UsersUpdateStatusRequest
from openapi_server.models.users_update_verification_request import UsersUpdateVerificationRequest
from openapi_server import util


async def users_create(request: web.Request, body=None) -> web.Response:
    """Create User

    Create a new user.

    :param body: 
    :type body: dict | bytes

    """
    body = UsersCreateRequest.from_dict(body)
    return web.Response(status=200)


async def users_delete(request: web.Request, user_id) -> web.Response:
    """Delete User

    Delete a user by its unique ID.

    :param user_id: User unique ID.
    :type user_id: str

    """
    return web.Response(status=200)


async def users_delete_session(request: web.Request, user_id, session_id) -> web.Response:
    """Delete User Session

    Delete a user sessions by its unique ID.

    :param user_id: User unique ID.
    :type user_id: str
    :param session_id: User unique session ID.
    :type session_id: str

    """
    return web.Response(status=200)


async def users_delete_sessions(request: web.Request, user_id) -> web.Response:
    """Delete User Sessions

    Delete all user&#39;s sessions by using the user&#39;s unique ID.

    :param user_id: User unique ID.
    :type user_id: str

    """
    return web.Response(status=200)


async def users_get(request: web.Request, user_id) -> web.Response:
    """Get User

    Get a user by its unique ID.

    :param user_id: User unique ID.
    :type user_id: str

    """
    return web.Response(status=200)


async def users_get_logs(request: web.Request, user_id) -> web.Response:
    """Get User Logs

    Get a user activity logs list by its unique ID.

    :param user_id: User unique ID.
    :type user_id: str

    """
    return web.Response(status=200)


async def users_get_prefs(request: web.Request, user_id) -> web.Response:
    """Get User Preferences

    Get the user preferences by its unique ID.

    :param user_id: User unique ID.
    :type user_id: str

    """
    return web.Response(status=200)


async def users_get_sessions(request: web.Request, user_id) -> web.Response:
    """Get User Sessions

    Get the user sessions list by its unique ID.

    :param user_id: User unique ID.
    :type user_id: str

    """
    return web.Response(status=200)


async def users_list(request: web.Request, search=None, limit=None, offset=None, order_type=None) -> web.Response:
    """List Users

    Get a list of all the project&#39;s users. You can use the query params to filter your results.

    :param search: Search term to filter your list results. Max length: 256 chars.
    :type search: str
    :param limit: Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
    :type limit: int
    :param offset: Results offset. The default value is 0. Use this param to manage pagination.
    :type offset: int
    :param order_type: Order result by ASC or DESC order.
    :type order_type: str

    """
    return web.Response(status=200)


async def users_update_prefs(request: web.Request, user_id, body=None) -> web.Response:
    """Update User Preferences

    Update the user preferences by its unique ID. You can pass only the specific settings you wish to update.

    :param user_id: User unique ID.
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AccountUpdatePrefsRequest.from_dict(body)
    return web.Response(status=200)


async def users_update_status(request: web.Request, user_id, body=None) -> web.Response:
    """Update User Status

    Update the user status by its unique ID.

    :param user_id: User unique ID.
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UsersUpdateStatusRequest.from_dict(body)
    return web.Response(status=200)


async def users_update_verification(request: web.Request, user_id, body=None) -> web.Response:
    """Update Email Verification

    Update the user email verification status by its unique ID.

    :param user_id: User unique ID.
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UsersUpdateVerificationRequest.from_dict(body)
    return web.Response(status=200)
