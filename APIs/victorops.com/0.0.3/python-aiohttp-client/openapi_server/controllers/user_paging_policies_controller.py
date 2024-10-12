from typing import List, Dict
from aiohttp import web

from openapi_server.models.policies import Policies
from openapi_server import util


async def api_public_v1_user_user_policies_get(request: web.Request, x_vo_api_id, x_vo_api_key, user) -> web.Response:
    """Get a list of paging policies for a user

    Get paging policies for a user  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param user: The VictorOps user ID
    :type user: str

    """
    return web.Response(status=200)
