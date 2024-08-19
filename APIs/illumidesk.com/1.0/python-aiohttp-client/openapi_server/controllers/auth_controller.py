from typing import List, Dict
from aiohttp import web

from openapi_server.models.jwt import JWT
from openapi_server.models.jwt_data import JWTData
from openapi_server.models.jwt_error import JWTError
from openapi_server.models.refresh_json_web_token import RefreshJSONWebToken
from openapi_server.models.refresh_json_web_token_data import RefreshJSONWebTokenData
from openapi_server.models.refresh_json_web_token_error import RefreshJSONWebTokenError
from openapi_server.models.user import User
from openapi_server.models.user_data import UserData
from openapi_server.models.user_error import UserError
from openapi_server.models.verify_json_web_token import VerifyJSONWebToken
from openapi_server.models.verify_json_web_token_data import VerifyJSONWebTokenData
from openapi_server.models.verify_json_web_token_error import VerifyJSONWebTokenError
from openapi_server import util


async def auth_jwt_token_auth(request: web.Request, jwt_data=None) -> web.Response:
    """Create JSON Web Token (JWT)

    

    :param jwt_data: 
    :type jwt_data: dict | bytes

    """
    jwt_data = JWTData.from_dict(jwt_data)
    return web.Response(status=200)


async def auth_jwt_token_refresh(request: web.Request, refreshjwt_data=None) -> web.Response:
    """Refresh a JSON Web Token (JWT)

    Obtains a new JSON Web Token using existing user credentials.

    :param refreshjwt_data: 
    :type refreshjwt_data: dict | bytes

    """
    refreshjwt_data = RefreshJSONWebTokenData.from_dict(refreshjwt_data)
    return web.Response(status=200)


async def auth_jwt_token_verify(request: web.Request, verifyjwt_data=None) -> web.Response:
    """Validate JSON Web Token (JWT)

    Checks veraciy of token.

    :param verifyjwt_data: 
    :type verifyjwt_data: dict | bytes

    """
    verifyjwt_data = VerifyJSONWebTokenData.from_dict(verifyjwt_data)
    return web.Response(status=200)


async def auth_register(request: web.Request, user_data=None) -> web.Response:
    """Register a user

    User registration requires confirming email address to activate user.

    :param user_data: 
    :type user_data: dict | bytes

    """
    user_data = UserData.from_dict(user_data)
    return web.Response(status=200)


async def oauth_login(request: web.Request, provider) -> web.Response:
    """oauth_login

    

    :param provider: OAuth2 provider
    :type provider: str

    """
    return web.Response(status=200)
