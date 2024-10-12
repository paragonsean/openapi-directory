from typing import List, Dict
from aiohttp import web

from openapi_server.models.oauth_v1_openid_discovery import OauthV1OpenidDiscovery
from openapi_server import util


async def fetch_openid_discovery(request: web.Request, ) -> web.Response:
    """fetch_openid_discovery

    Fetch configuration details about the OpenID Connect Authorization Server


    """
    return web.Response(status=200)
