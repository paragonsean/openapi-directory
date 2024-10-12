from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_authenticated_user import APIModelsAuthenticatedUser
from openapi_server.models.api_models_credentials import APIModelsCredentials
from openapi_server.models.api_models_password_reset import APIModelsPasswordReset
from openapi_server.models.api_models_password_reset_request import APIModelsPasswordResetRequest
from openapi_server.models.api_models_token_options import APIModelsTokenOptions
from openapi_server import util


async def authentication_default(request: web.Request, body) -> web.Response:
    """Authenticate a user.

    No Documentation Found.

    :param body: Create a user account.
    :type body: dict | bytes

    """
    body = APIModelsCredentials.from_dict(body)
    return web.Response(status=200)


async def authentication_is_alive(request: web.Request, ) -> web.Response:
    """Acknowledges the connection to the API

    No Documentation Found.


    """
    return web.Response(status=200)


async def authentication_put_manage_tokens(request: web.Request, user_id, body) -> web.Response:
    """Manage API tokens.

    No Documentation Found.

    :param user_id: 
    :type user_id: int
    :param body: The options for token management.
    :type body: dict | bytes

    """
    body = APIModelsTokenOptions.from_dict(body)
    return web.Response(status=200)


async def authentication_request_password_reset(request: web.Request, body) -> web.Response:
    """Request a password reset.

    No Documentation Found.

    :param body: The password reset request.
    :type body: dict | bytes

    """
    body = APIModelsPasswordResetRequest.from_dict(body)
    return web.Response(status=200)


async def authentication_reset_pasword(request: web.Request, body) -> web.Response:
    """Reset a password

    No Documentation Found.

    :param body: The password reset detail.
    :type body: dict | bytes

    """
    body = APIModelsPasswordReset.from_dict(body)
    return web.Response(status=200)
