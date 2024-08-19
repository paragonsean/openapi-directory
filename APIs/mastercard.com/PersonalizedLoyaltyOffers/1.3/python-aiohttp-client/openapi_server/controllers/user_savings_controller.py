from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.user_savings_response import UserSavingsResponse
from openapi_server import util


async def usersavings_get(request: web.Request, fid, user_token) -> web.Response:
    """Returns Savings for the User

    This resource returns the accumulated and potential savings for a Personalized Offers user. 

    :param fid: Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
    :type fid: str
    :param user_token: Session identifier as returned by the UserToken resource.
    :type user_token: str

    """
    return web.Response(status=200)
