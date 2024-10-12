from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def admin_users_session_invalidate(request: web.Request, token, session_id, team_id) -> web.Response:
    """admin_users_session_invalidate

    Invalidate a single session for a user by session_id

    :param token: Authentication token. Requires scope: &#x60;admin.users:write&#x60;
    :type token: str
    :param session_id: 
    :type session_id: int
    :param team_id: ID of the team that the session belongs to
    :type team_id: str

    """
    return web.Response(status=200)


async def admin_users_session_reset(request: web.Request, token, user_id, mobile_only=None, web_only=None) -> web.Response:
    """admin_users_session_reset

    Wipes all valid sessions on all devices for a given user

    :param token: Authentication token. Requires scope: &#x60;admin.users:write&#x60;
    :type token: str
    :param user_id: The ID of the user to wipe sessions for
    :type user_id: str
    :param mobile_only: Only expire mobile sessions (default: false)
    :type mobile_only: bool
    :param web_only: Only expire web sessions (default: false)
    :type web_only: bool

    """
    return web.Response(status=200)
