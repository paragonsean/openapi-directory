from typing import List, Dict
from aiohttp import web

from openapi_server.models.user_authentication import UserAuthentication
from openapi_server.models.user_full_profile import UserFullProfile
from openapi_server import util


async def authentication_post(request: web.Request, user) -> web.Response:
    """Sign in user

    Sign in user. Wrap authentication parameters in [user].

    :param user: user authentication attributes
    :type user: dict | bytes

    """
    user = UserAuthentication.from_dict(user)
    return web.Response(status=200)
