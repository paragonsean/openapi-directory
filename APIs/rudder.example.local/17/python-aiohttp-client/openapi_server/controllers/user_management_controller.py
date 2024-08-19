from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_user200_response import AddUser200Response
from openapi_server.models.delete_user200_response import DeleteUser200Response
from openapi_server.models.get_role200_response import GetRole200Response
from openapi_server.models.get_user_info200_response import GetUserInfo200Response
from openapi_server.models.reload_user_conf200_response import ReloadUserConf200Response
from openapi_server.models.update_user200_response import UpdateUser200Response
from openapi_server.models.users import Users
from openapi_server import util


async def add_user(request: web.Request, body) -> web.Response:
    """Add user

    Add a new user

    :param body: 
    :type body: dict | bytes

    """
    body = Users.from_dict(body)
    return web.Response(status=200)


async def delete_user(request: web.Request, username) -> web.Response:
    """Delete an user

    Delete the user and his permissions

    :param username: Username of an user (unique)
    :type username: str

    """
    return web.Response(status=200)


async def get_role(request: web.Request, ) -> web.Response:
    """List all roles

    Get all available roles and their rights


    """
    return web.Response(status=200)


async def get_user_info(request: web.Request, ) -> web.Response:
    """List all users

    Get the list of all present users and their permissions


    """
    return web.Response(status=200)


async def reload_user_conf(request: web.Request, ) -> web.Response:
    """Reload user

    Reload the users from the file system, in the configuration file


    """
    return web.Response(status=200)


async def update_user(request: web.Request, username, body) -> web.Response:
    """Update user&#39;s infos

    Rename, change password (pre-hashed or not) and change permission of an user. If a parameter is empty, it will be ignored.

    :param username: Username of an user (unique)
    :type username: str
    :param body: 
    :type body: dict | bytes

    """
    body = Users.from_dict(body)
    return web.Response(status=200)
