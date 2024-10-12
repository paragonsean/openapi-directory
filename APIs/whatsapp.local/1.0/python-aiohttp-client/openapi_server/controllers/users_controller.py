from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_user_request_body import CreateUserRequestBody
from openapi_server.models.detailed_user_response import DetailedUserResponse
from openapi_server.models.login_admin_request_body import LoginAdminRequestBody
from openapi_server.models.update_user_request_body import UpdateUserRequestBody
from openapi_server.models.user_login_response import UserLoginResponse
from openapi_server.models.user_response import UserResponse
from openapi_server import util


async def create_user(request: web.Request, body) -> web.Response:
    """Create-User

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateUserRequestBody.from_dict(body)
    return web.Response(status=200)


async def delete_user(request: web.Request, user_username) -> web.Response:
    """Delete-User

    

    :param user_username: 
    :type user_username: str

    """
    return web.Response(status=200)


async def get_user(request: web.Request, user_username) -> web.Response:
    """Get-User

    

    :param user_username: 
    :type user_username: str

    """
    return web.Response(status=200)


async def login_user(request: web.Request, body=None) -> web.Response:
    """Login-User

    

    :param body: 
    :type body: dict | bytes

    """
    body = LoginAdminRequestBody.from_dict(body)
    return web.Response(status=200)


async def logout_user(request: web.Request, ) -> web.Response:
    """Logout-User

    


    """
    return web.Response(status=200)


async def update_user(request: web.Request, user_username, body) -> web.Response:
    """Update-User

    

    :param user_username: 
    :type user_username: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateUserRequestBody.from_dict(body)
    return web.Response(status=200)
