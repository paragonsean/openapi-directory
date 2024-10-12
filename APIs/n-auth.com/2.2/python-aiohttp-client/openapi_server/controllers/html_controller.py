from typing import List, Dict
from aiohttp import web

from openapi_server.models.html_footer_body import HtmlFooterBody
from openapi_server.models.login_status import LoginStatus
from openapi_server.models.user_context import UserContext
from openapi_server import util


async def get_html_enrol(request: web.Request, serverid, x_nonce, name=None, userid=None) -> web.Response:
    """Generate HTML to enrol a new user

    Generate HTML to enrol a new user. Required permission: &#39;sessions&#39;. 

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param x_nonce: Nonce to identify the browser/webserver session
    :type x_nonce: str
    :param name: Name to forward to the nextAuth app for this account
    :type name: str
    :param userid: User name to register this user under
    :type userid: str

    """
    return web.Response(status=200)


async def get_html_footer(request: web.Request, serverid, x_nonce, html_footer_body=None) -> web.Response:
    """Generic HTML to add to footer. Required for login/logout/enrol functionality.

    HTML to add to footer of HTML page. Required permission: &#39;sessions&#39;. 

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param x_nonce: Nonce to identify the browser/webserver session
    :type x_nonce: str
    :param html_footer_body: Additional sessions that should be monitored through the websocket.
    :type html_footer_body: dict | bytes

    """
    html_footer_body = HtmlFooterBody.from_dict(html_footer_body)
    return web.Response(status=200)


async def get_html_login(request: web.Request, serverid, x_nonce, user_context=None) -> web.Response:
    """Generate HTML for the login block

    Generate HTML for the login block. Required permission: &#39;sessions&#39;. 

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param x_nonce: Nonce to identify the browser/webserver session
    :type x_nonce: str
    :param user_context: Session information to display to user.
    :type user_context: dict | bytes

    """
    user_context = UserContext.from_dict(user_context)
    return web.Response(status=200)


async def get_session_0(request: web.Request, serverid, x_nonce) -> web.Response:
    """Check if the user is logged in

    Based on the browser/webserver session identifier, check if the user is logged in and return the associated username. This also returns additional information: the data for the login qr code and whether or not a loggin can be provoked directly from the server. Required permission: &#39;sessions&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param x_nonce: Nonce to identify the browser/webserver session
    :type x_nonce: str

    """
    return web.Response(status=200)


async def logout_0(request: web.Request, serverid, x_nonce) -> web.Response:
    """Force a logout on the given session

    Force a logout on the given session. Required permission: &#39;sessions&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param x_nonce: Nonce to identify the browser/webserver session
    :type x_nonce: str

    """
    return web.Response(status=200)
