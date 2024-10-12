from typing import List, Dict
from aiohttp import web

from openapi_server.models.session_entity import SessionEntity
from openapi_server import util


async def delete_sessions(request: web.Request, ) -> web.Response:
    """Delete user session (log out)

    Delete user session (log out)


    """
    return web.Response(status=200)


async def post_sessions(request: web.Request, otp=None, partial_session_id=None, password=None, username=None) -> web.Response:
    """Create user session (log in)

    Create user session (log in)

    :param otp: If this user has a 2FA device, provide its OTP or code here.
    :type otp: str
    :param partial_session_id: Identifier for a partially-completed login
    :type partial_session_id: str
    :param password: Password for sign in
    :type password: str
    :param username: Username to sign in as
    :type username: str

    """
    return web.Response(status=200)
