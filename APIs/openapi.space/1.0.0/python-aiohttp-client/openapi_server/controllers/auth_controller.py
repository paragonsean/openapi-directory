from typing import List, Dict
from aiohttp import web

from openapi_server.models.credentials import Credentials
from openapi_server.models.login_apinf_request import LoginApinfRequest
from openapi_server.models.login_apinf_token_request import LoginApinfTokenRequest
from openapi_server.models.login_token import LoginToken
from openapi_server.models.registration import Registration
from openapi_server import util


async def login(request: web.Request, body=None) -> web.Response:
    """Log in to OpenAPI space

    

    :param body: the user credentials
    :type body: dict | bytes

    """
    body = Credentials.from_dict(body)
    return web.Response(status=200)


async def login_apinf(request: web.Request, body=None) -> web.Response:
    """Log in to OpenAPI space using an APInf account

    

    :param body: the APInf username and password
    :type body: dict | bytes

    """
    body = LoginApinfRequest.from_dict(body)
    return web.Response(status=200)


async def login_apinf_token(request: web.Request, body=None) -> web.Response:
    """Log in to OpenAPI space using an APInf authentication token

    

    :param body: the APInf authentication token and user ID
    :type body: dict | bytes

    """
    body = LoginApinfTokenRequest.from_dict(body)
    return web.Response(status=200)


async def logout(request: web.Request, ) -> web.Response:
    """Log out from OpenAPI space

    


    """
    return web.Response(status=200)


async def ping(request: web.Request, ) -> web.Response:
    """Check whether or not you are authenticated

    


    """
    return web.Response(status=200)


async def register(request: web.Request, body=None) -> web.Response:
    """Register to OpenAPI space

    

    :param body: registration details
    :type body: dict | bytes

    """
    body = Registration.from_dict(body)
    return web.Response(status=200)
