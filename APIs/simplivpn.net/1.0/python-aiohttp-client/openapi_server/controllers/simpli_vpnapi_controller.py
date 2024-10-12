from typing import List, Dict
from aiohttp import web

from openapi_server.models.disable_user import DisableUser
from openapi_server.models.enable_user import EnableUser
from openapi_server.models.register import Register
from openapi_server.models.user_login import UserLogin
from openapi_server import util


async def disable_user(request: web.Request, body) -> web.Response:
    """DisableUser

    This route allows you to disable a user&#39;s vpn access.

    :param body: 
    :type body: dict | bytes

    """
    body = DisableUser.from_dict(body)
    return web.Response(status=200)


async def enable_user(request: web.Request, body) -> web.Response:
    """EnableUser

    This route allows you to enable a user&#39;s vpn access. This route can only be called using your user&#39;s Bearer Auth token.

    :param body: 
    :type body: dict | bytes

    """
    body = EnableUser.from_dict(body)
    return web.Response(status=200)


async def get_server_summaries(request: web.Request, ) -> web.Response:
    """get_server_summaries

    


    """
    return web.Response(status=200)


async def get_servers(request: web.Request, ) -> web.Response:
    """get_servers

    


    """
    return web.Response(status=200)


async def login(request: web.Request, body) -> web.Response:
    """Login

    This route allows you to login a user. The response will give you a Bearer auth token to use with all rquests pertaining to the user. This token expires in 7 days, so for every request you should check if you get an unauthorized responsve and re-validate the login if needed.

    :param body: 
    :type body: dict | bytes

    """
    body = UserLogin.from_dict(body)
    return web.Response(status=200)


async def register(request: web.Request, body) -> web.Response:
    """Register

    This route allows VPN Admin user&#39;s with an api key to register a vpn user account. This route can only be called using your api key supplied to you from SimpliVPN. Before calling this you should use your api key to call the /UsernameAvailable route to make sure the username you want is available first. All subsequent user requests following can be done using the user&#39;s api token, their token&#39;s expire every 7 days, so you should occasionally check them and if you get unauthorized, refresh their token by calling /login route. This route will also auto-enable a new user.

    :param body: 
    :type body: dict | bytes

    """
    body = Register.from_dict(body)
    return web.Response(status=200)


async def username_available(request: web.Request, body) -> web.Response:
    """UsernameAvailable

    This route allows VPN Admin user&#39;s to check if a specific username is available before registering an account username. This route can only be called using your api key supplied to you from SimpliVPN.

    :param body: 
    :type body: dict | bytes

    """
    body = EnableUser.from_dict(body)
    return web.Response(status=200)
