from typing import List, Dict
from aiohttp import web

from openapi_server.models.authentiq_id import AuthentiqID
from openapi_server.models.claims import Claims
from openapi_server.models.error import Error
from openapi_server.models.key_bind200_response import KeyBind200Response
from openapi_server.models.key_register201_response import KeyRegister201Response
from openapi_server.models.push_login_request200_response import PushLoginRequest200Response
from openapi_server.models.push_token import PushToken
from openapi_server.models.sign_request201_response import SignRequest201Response
from openapi_server import util


async def key_register_0(request: web.Request, body) -> web.Response:
    """key_register_0

    Register a new ID &#x60;JWT(sub, devtoken)&#x60;  v5: &#x60;JWT(sub, pk, devtoken, ...)&#x60;  See: https://github.com/skion/authentiq/wiki/JWT-Examples 

    :param body: Authentiq ID to register
    :type body: dict | bytes

    """
    body = AuthentiqID.from_dict(body)
    return web.Response(status=200)


async def key_update_0(request: web.Request, pk, body) -> web.Response:
    """key_update_0

    update properties of an Authentiq ID. (not operational in v4; use PUT for now)  v5: POST issuer-signed email &amp; phone scopes in a self-signed JWT  See: https://github.com/skion/authentiq/wiki/JWT-Examples 

    :param pk: Public Signing Key - Authentiq ID (43 chars)
    :type pk: str
    :param body: Authentiq ID to register
    :type body: dict | bytes

    """
    body = AuthentiqID.from_dict(body)
    return web.Response(status=200)


async def push_login_request_0(request: web.Request, param_callback, body) -> web.Response:
    """push_login_request_0

    push sign-in request See: https://github.com/skion/authentiq/wiki/JWT-Examples 

    :param param_callback: URI App will connect to
    :type param_callback: str
    :param body: Push Token.
    :type body: dict | bytes

    """
    body = PushToken.from_dict(body)
    return web.Response(status=200)


async def sign_confirm_0(request: web.Request, job) -> web.Response:
    """sign_confirm_0

    this is a scope confirmation

    :param job: Job ID (20 chars)
    :type job: str

    """
    return web.Response(status=200)


async def sign_request_0(request: web.Request, body, test=None) -> web.Response:
    """sign_request_0

    scope verification request See: https://github.com/skion/authentiq/wiki/JWT-Examples 

    :param body: Claims of scope
    :type body: dict | bytes
    :param test: test only mode, using test issuer
    :type test: int

    """
    body = Claims.from_dict(body)
    return web.Response(status=200)
