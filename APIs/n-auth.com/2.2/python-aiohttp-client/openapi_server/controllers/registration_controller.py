from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server import util


async def get_qr_enrol(request: web.Request, serverid, x_nonce, name, userid=None, img=None, s=None) -> web.Response:
    """Generate data for an enrol qr code

    Returns the data for an enrol qr code. Required permission: &#39;sessions&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param x_nonce: Nonce to identify the browser/webserver session
    :type x_nonce: str
    :param name: Name to forward to the nextAuth app for this account
    :type name: str
    :param userid: User name to register this user under
    :type userid: str
    :param img: &#39;png&#39; for a PNG image, not set for raw data in the qr code
    :type img: str
    :param s: size in pixels of the qr code, defaults to 500
    :type s: int

    """
    return web.Response(status=200)


async def get_server_vash(request: web.Request, serverid) -> web.Response:
    """Visual hash of this server

    Returns a PNG of the visual hash corresponding to this server. This visual hash is used during the registration process (optional), for the user to verify that (s)he is registering with the right server in the nextAuth app. For single-server nextAuth-enabled apps (white label or mobile SDK), the public key of the server is typically pinned within the app and hence this visual hash is not displayed to the user. Required permission: &#39;sessions&#39; or &#39;servers&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str

    """
    return web.Response(status=200)


async def register_user_0(request: web.Request, serverid, x_nonce, userid) -> web.Response:
    """Register a userid for the currently logged in account.

    Register a user for the currently logged in account. You can also directly pass a user name when generating an ENROL qr code. Required permission: &#39;users&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param x_nonce: Nonce to identify the browser/webserver session
    :type x_nonce: str
    :param userid: Username to register
    :type userid: str

    """
    return web.Response(status=200)


async def update_account_user_0(request: web.Request, serverid, accountid, userid) -> web.Response:
    """Update user of the given account.

    Update the user of the given account. Required permission: &#39;accounts&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param accountid: Account id
    :type accountid: int
    :param userid: User name
    :type userid: str

    """
    return web.Response(status=200)
