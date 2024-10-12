from typing import List, Dict
from aiohttp import web

from openapi_server.models.oauth_v1_certs import OauthV1Certs
from openapi_server import util


async def fetch_certs(request: web.Request, ) -> web.Response:
    """fetch_certs

    Fetches public JWKs


    """
    return web.Response(status=200)
