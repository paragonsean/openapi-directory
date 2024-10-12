from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_v1_secondary_auth_token import AccountsV1SecondaryAuthToken
from openapi_server import util


async def create_secondary_auth_token(request: web.Request, ) -> web.Response:
    """create_secondary_auth_token

    Create a new secondary Auth Token


    """
    return web.Response(status=200)


async def delete_secondary_auth_token(request: web.Request, ) -> web.Response:
    """delete_secondary_auth_token

    Delete the secondary Auth Token from your account


    """
    return web.Response(status=200)
