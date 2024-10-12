from typing import List, Dict
from aiohttp import web

from openapi_server.models.certs import Certs
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.open_id_configuration import OpenIdConfiguration
from openapi_server.models.session_request import SessionRequest
from openapi_server.models.session_response import SessionResponse
from openapi_server import util


async def v05_certs_get(request: web.Request, ) -> web.Response:
    """Get certs for JWT verification

    


    """
    return web.Response(status=200)


async def v05_sessions_post(request: web.Request, body) -> web.Response:
    """Get access token

    

    :param body: 
    :type body: dict | bytes

    """
    body = SessionRequest.from_dict(body)
    return web.Response(status=200)


async def v05_well_known_openid_configuration_get(request: web.Request, ) -> web.Response:
    """Get openid configuration

    


    """
    return web.Response(status=200)
