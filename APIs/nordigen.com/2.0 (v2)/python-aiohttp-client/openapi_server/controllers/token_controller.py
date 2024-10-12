from typing import List, Dict
from aiohttp import web

from openapi_server.models.jwt_obtain_pair_request import JWTObtainPairRequest
from openapi_server.models.jwt_refresh_request import JWTRefreshRequest
from openapi_server.models.spectacular_jwt_obtain import SpectacularJWTObtain
from openapi_server.models.spectacular_jwt_refresh import SpectacularJWTRefresh
from openapi_server import util


async def j_wt_obtain(request: web.Request, body) -> web.Response:
    """j_wt_obtain

    Obtain JWT pair

    :param body: 
    :type body: dict | bytes

    """
    body = JWTObtainPairRequest.from_dict(body)
    return web.Response(status=200)


async def j_wt_refresh(request: web.Request, body) -> web.Response:
    """j_wt_refresh

    Refresh access token

    :param body: 
    :type body: dict | bytes

    """
    body = JWTRefreshRequest.from_dict(body)
    return web.Response(status=200)
