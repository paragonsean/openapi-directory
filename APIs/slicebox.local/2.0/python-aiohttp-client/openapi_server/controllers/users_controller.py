from typing import List, Dict
from aiohttp import web

from openapi_server.models.new_user import NewUser
from openapi_server.models.user import User
from openapi_server.models.user_info import UserInfo
from openapi_server.models.user_pass import UserPass
from openapi_server import util


async def users_current_get(request: web.Request, ) -> web.Response:
    """users_current_get

    obtain information on the currently logged in user as specified by the supplied session cookie, IP address and user agent.


    """
    return web.Response(status=200)


async def users_get(request: web.Request, startindex=None, count=None) -> web.Response:
    """users_get

    Returns all users of slicebox

    :param startindex: start index of returned slice of users
    :type startindex: int
    :param count: size of returned slice of users
    :type count: int

    """
    return web.Response(status=200)


async def users_id_delete(request: web.Request, id) -> web.Response:
    """users_id_delete

    deletes a single user based on the ID supplied

    :param id: ID of user to delete
    :type id: int

    """
    return web.Response(status=200)


async def users_login_post(request: web.Request, user_pass) -> web.Response:
    """users_login_post

    Obtain a session cookie that can be used to authenticate future API calls from the present IP address and with the present user agent.

    :param user_pass: username and password for user logging in
    :type user_pass: dict | bytes

    """
    user_pass = UserPass.from_dict(user_pass)
    return web.Response(status=200)


async def users_logout_post(request: web.Request, ) -> web.Response:
    """users_logout_post

    Logout the current user by responding with a delete cookie header removing the session cookie for this user.


    """
    return web.Response(status=200)


async def users_post(request: web.Request, user) -> web.Response:
    """users_post

    Creates a new user. Dupicates are accepted but not added.

    :param user: User to add
    :type user: dict | bytes

    """
    user = NewUser.from_dict(user)
    return web.Response(status=200)
