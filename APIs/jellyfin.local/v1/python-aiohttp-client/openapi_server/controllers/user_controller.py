from typing import List, Dict
from aiohttp import web

from openapi_server.models.authenticate_user_by_name import AuthenticateUserByName
from openapi_server.models.authentication_result import AuthenticationResult
from openapi_server.models.create_user_by_name import CreateUserByName
from openapi_server.models.forgot_password_dto import ForgotPasswordDto
from openapi_server.models.forgot_password_result import ForgotPasswordResult
from openapi_server.models.pin_redeem_result import PinRedeemResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.quick_connect_dto import QuickConnectDto
from openapi_server.models.update_user_easy_password import UpdateUserEasyPassword
from openapi_server.models.update_user_password import UpdateUserPassword
from openapi_server.models.user_configuration import UserConfiguration
from openapi_server.models.user_dto import UserDto
from openapi_server.models.user_policy import UserPolicy
from openapi_server import util


async def authenticate_user(request: web.Request, user_id, pw, password=None) -> web.Response:
    """Authenticates a user.

    

    :param user_id: The user id.
    :type user_id: str
    :type user_id: str
    :param pw: The password as plain text.
    :type pw: str
    :param password: The password sha1-hash.
    :type password: str

    """
    return web.Response(status=200)


async def authenticate_user_by_name(request: web.Request, body) -> web.Response:
    """Authenticates a user by name.

    

    :param body: The M:Jellyfin.Api.Controllers.UserController.AuthenticateUserByName(Jellyfin.Api.Models.UserDtos.AuthenticateUserByName) request.
    :type body: dict | bytes

    """
    body = AuthenticateUserByName.from_dict(body)
    return web.Response(status=200)


async def authenticate_with_quick_connect(request: web.Request, body) -> web.Response:
    """Authenticates a user with quick connect.

    

    :param body: The Jellyfin.Api.Models.UserDtos.QuickConnectDto request.
    :type body: dict | bytes

    """
    body = QuickConnectDto.from_dict(body)
    return web.Response(status=200)


async def create_user_by_name(request: web.Request, body) -> web.Response:
    """Creates a user.

    

    :param body: The create user by name request body.
    :type body: dict | bytes

    """
    body = CreateUserByName.from_dict(body)
    return web.Response(status=200)


async def delete_user(request: web.Request, user_id) -> web.Response:
    """Deletes a user.

    

    :param user_id: The user id.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def forgot_password(request: web.Request, body) -> web.Response:
    """Initiates the forgot password process for a local user.

    

    :param body: The forgot password request containing the entered username.
    :type body: dict | bytes

    """
    body = ForgotPasswordDto.from_dict(body)
    return web.Response(status=200)


async def forgot_password_pin(request: web.Request, body=None) -> web.Response:
    """Redeems a forgot password pin.

    

    :param body: The pin.
    :type body: str

    """
    return web.Response(status=200)


async def get_current_user(request: web.Request, ) -> web.Response:
    """Gets the user based on auth token.

    


    """
    return web.Response(status=200)


async def get_public_users(request: web.Request, ) -> web.Response:
    """Gets a list of publicly visible users for display on a login screen.

    


    """
    return web.Response(status=200)


async def get_user_by_id(request: web.Request, user_id) -> web.Response:
    """Gets a user by Id.

    

    :param user_id: The user id.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def get_users(request: web.Request, is_hidden=None, is_disabled=None) -> web.Response:
    """Gets a list of users.

    

    :param is_hidden: Optional filter by IsHidden&#x3D;true or false.
    :type is_hidden: bool
    :param is_disabled: Optional filter by IsDisabled&#x3D;true or false.
    :type is_disabled: bool

    """
    return web.Response(status=200)


async def update_user(request: web.Request, user_id, body) -> web.Response:
    """Updates a user.

    

    :param user_id: The user id.
    :type user_id: str
    :type user_id: str
    :param body: The updated user model.
    :type body: dict | bytes

    """
    body = UserDto.from_dict(body)
    return web.Response(status=200)


async def update_user_configuration(request: web.Request, user_id, body) -> web.Response:
    """Updates a user configuration.

    

    :param user_id: The user id.
    :type user_id: str
    :type user_id: str
    :param body: The new user configuration.
    :type body: dict | bytes

    """
    body = UserConfiguration.from_dict(body)
    return web.Response(status=200)


async def update_user_easy_password(request: web.Request, user_id, body) -> web.Response:
    """Updates a user&#39;s easy password.

    

    :param user_id: The user id.
    :type user_id: str
    :type user_id: str
    :param body: The M:Jellyfin.Api.Controllers.UserController.UpdateUserEasyPassword(System.Guid,Jellyfin.Api.Models.UserDtos.UpdateUserEasyPassword) request.
    :type body: dict | bytes

    """
    body = UpdateUserEasyPassword.from_dict(body)
    return web.Response(status=200)


async def update_user_password(request: web.Request, user_id, body) -> web.Response:
    """Updates a user&#39;s password.

    

    :param user_id: The user id.
    :type user_id: str
    :type user_id: str
    :param body: The M:Jellyfin.Api.Controllers.UserController.UpdateUserPassword(System.Guid,Jellyfin.Api.Models.UserDtos.UpdateUserPassword) request.
    :type body: dict | bytes

    """
    body = UpdateUserPassword.from_dict(body)
    return web.Response(status=200)


async def update_user_policy(request: web.Request, user_id, body) -> web.Response:
    """Updates a user policy.

    

    :param user_id: The user id.
    :type user_id: str
    :type user_id: str
    :param body: The new user policy.
    :type body: dict | bytes

    """
    body = UserPolicy.from_dict(body)
    return web.Response(status=200)
