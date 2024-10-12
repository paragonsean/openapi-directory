from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.push_login_request200_response import PushLoginRequest200Response
from openapi_server.models.push_token import PushToken
from openapi_server import util


async def push_login_request(request: web.Request, param_callback, body) -> web.Response:
    """push_login_request

    push sign-in request See: https://github.com/skion/authentiq/wiki/JWT-Examples 

    :param param_callback: URI App will connect to
    :type param_callback: str
    :param body: Push Token.
    :type body: dict | bytes

    """
    body = PushToken.from_dict(body)
    return web.Response(status=200)
