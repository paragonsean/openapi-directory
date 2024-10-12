from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_credential import AccessCredential
from openapi_server.models.account import Account
from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.user import User
from openapi_server import util


async def add_credential(request: web.Request, body) -> web.Response:
    """add/replace credential

    

    :param body: 
    :type body: dict | bytes

    """
    body = AccessCredential.from_dict(body)
    return web.Response(status=200)


async def get_credentials(request: web.Request, ) -> web.Response:
    """Get current credential summary

    


    """
    return web.Response(status=200)


async def get_user(request: web.Request, ) -> web.Response:
    """List authenticated user info

    


    """
    return web.Response(status=200)


async def get_users_account(request: web.Request, ) -> web.Response:
    """List the account for the authenticated user

    


    """
    return web.Response(status=200)
