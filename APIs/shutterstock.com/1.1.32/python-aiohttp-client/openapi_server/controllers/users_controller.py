from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_token_details import AccessTokenDetails
from openapi_server.models.subscription_data_list import SubscriptionDataList
from openapi_server.models.user_details import UserDetails
from openapi_server import util


async def get_access_token(request: web.Request, ) -> web.Response:
    """Get access token details

    


    """
    return web.Response(status=200)


async def get_user(request: web.Request, ) -> web.Response:
    """Get user details

    


    """
    return web.Response(status=200)


async def get_user_subscription_list(request: web.Request, ) -> web.Response:
    """List user subscriptions

    


    """
    return web.Response(status=200)
