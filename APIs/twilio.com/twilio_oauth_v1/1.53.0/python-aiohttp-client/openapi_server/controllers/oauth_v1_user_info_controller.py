from typing import List, Dict
from aiohttp import web

from openapi_server.models.oauth_v1_user_info import OauthV1UserInfo
from openapi_server import util


async def fetch_user_info(request: web.Request, ) -> web.Response:
    """fetch_user_info

    Retrieves the consented UserInfo and other claims about the logged-in subject (end-user).


    """
    return web.Response(status=200)
