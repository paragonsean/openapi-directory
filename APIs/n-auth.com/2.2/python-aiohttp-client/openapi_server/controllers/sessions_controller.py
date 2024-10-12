from typing import List, Dict
from aiohttp import web

from openapi_server.models.login_status import LoginStatus
from openapi_server.models.user_context import UserContext
from openapi_server import util


async def get_qr_login(request: web.Request, serverid, x_nonce, img=None, s=None, user_context=None) -> web.Response:
    """Generate data for a login qr code

    Returns the data for a login qr code. Required permission: &#39;sessions&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param x_nonce: Nonce to identify the browser/webserver session
    :type x_nonce: str
    :param img: \&quot;png\&quot; for a PNG image, not set for raw data in the qr code
    :type img: str
    :param s: size in pixels of the qr code, defaults to 500
    :type s: int
    :param user_context: Session information to display to user.
    :type user_context: dict | bytes

    """
    user_context = UserContext.from_dict(user_context)
    return web.Response(status=200)


async def get_session(request: web.Request, serverid, x_nonce) -> web.Response:
    """Check if the user is logged in

    Based on the browser/webserver session identifier, check if the user is logged in and return the associated username. This also returns additional information: the data for the login qr code and whether or not a loggin can be provoked directly from the server. Required permission: &#39;sessions&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param x_nonce: Nonce to identify the browser/webserver session
    :type x_nonce: str

    """
    return web.Response(status=200)


async def logout(request: web.Request, serverid, x_nonce) -> web.Response:
    """Force a logout on the given session

    Force a logout on the given session. Required permission: &#39;sessions&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param x_nonce: Nonce to identify the browser/webserver session
    :type x_nonce: str

    """
    return web.Response(status=200)


async def provoke_login(request: web.Request, serverid, x_nonce, user_context=None) -> web.Response:
    """Push a login confirmation to the user&#39;s app

    Push a login to the nextAuth app for the user to confirm, based on last account that successfully logged in for the given session. Required permission: &#39;sessions&#39;. 

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param x_nonce: Nonce to identify the browser/webserver session
    :type x_nonce: str
    :param user_context: Session information to display to user.
    :type user_context: dict | bytes

    """
    user_context = UserContext.from_dict(user_context)
    return web.Response(status=200)


async def provoke_login_on_account(request: web.Request, serverid, x_nonce, accountid, user_context=None) -> web.Response:
    """Push a login confirmation to the user&#39;s app

    Push a login to the nextAuth app for the user to confirm, based on the given account (app instance). Required permission: &#39;sessions&#39; or &#39;accounts&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param x_nonce: Base64 encoded nonce to identify the browser/webserver session
    :type x_nonce: str
    :param accountid: Account id
    :type accountid: int
    :param user_context: Session information to display to user
    :type user_context: dict | bytes

    """
    user_context = UserContext.from_dict(user_context)
    return web.Response(status=200)


async def provoke_login_on_user(request: web.Request, serverid, x_nonce, userid, user_context=None) -> web.Response:
    """Push a login confirmation to the user&#39;s app

    Push a login to the nextAuth app for the user to confirm, based on the given userid. Required permission: &#39;sessions&#39; or &#39;users&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param x_nonce: Nonce to identify the browser/webserver session
    :type x_nonce: str
    :param userid: User name
    :type userid: str
    :param user_context: Session information to display to user.
    :type user_context: dict | bytes

    """
    user_context = UserContext.from_dict(user_context)
    return web.Response(status=200)
